### SETUP
import matplotlib.pyplot as plt
from sklearn.metrics import PrecisionRecallDisplay
import numpy as np
import requests

# Need to change for every request
QUERY_URL = "http://localhost:8983/solr/articles/select?defType=edismax&indent=true&q.op=AND&q=Astronaut%20working%20ISS&qf=title%20content%20tags%20sections&rows=25"
QUERY_BOOST_URL = "http://localhost:8983/solr/articles/select?defType=edismax&indent=true&q.op=AND&q=Astronaut%20working%20ISS&qf=title^10%20content%20tags^5%20sections&rows=25"

QRELS_FILE = "./queries/q4/qrels.txt"

_, ax = plt.subplots(figsize=(5, 4))

# Read qrels to extract relevant documents
relevant = list(map(lambda el: el.strip(), open(QRELS_FILE).readlines()))

# Get query results from Solr instance
results = requests.get(QUERY_URL).json()["response"]["docs"]


### PRECISION-RECALL CURVE

# Calculate precision and recall values as we move down the ranked list
precision_values = [
    len([doc for doc in results[:idx] if doc["title"] in relevant]) / idx
    for idx, _ in enumerate(results, start=1)
]

recall_values = [
    len([doc for doc in results[:idx] if doc["title"] in relevant]) / len(relevant)
    for idx, _ in enumerate(results, start=1)
]

precision_recall_match = {k: v for k, v in zip(recall_values, precision_values)}

# Extend recall_values to include traditional steps for a better curve (0.1, 0.2 ...)
recall_values.extend(
    [step for step in np.arange(0, 1.1, 0.2) if step not in recall_values]
)
recall_values = sorted(set(recall_values))

# Extend matching dict to include these new intermediate steps
for idx, step in enumerate(recall_values):
    if step not in precision_recall_match:
        if idx > 0 and recall_values[idx - 1] in precision_recall_match:
            precision_recall_match[step] = precision_recall_match[
                recall_values[idx - 1]
            ]
        else:
            precision_recall_match[step] = precision_recall_match[
                recall_values[idx + 1]
            ]

disp = PrecisionRecallDisplay(
    [precision_recall_match.get(r) for r in recall_values], recall_values
)
disp.plot(ax=ax, name="Regular", color="cornflowerblue")

# Get query results from Solr instance
results = requests.get(QUERY_BOOST_URL).json()["response"]["docs"]


### PRECISION-RECALL CURVE

# Calculate precision and recall values as we move down the ranked list
precision_values = [
    len([doc for doc in results[:idx] if doc["title"] in relevant]) / idx
    for idx, _ in enumerate(results, start=1)
]

recall_values = [
    len([doc for doc in results[:idx] if doc["title"] in relevant]) / len(relevant)
    for idx, _ in enumerate(results, start=1)
]

precision_recall_match = {k: v for k, v in zip(recall_values, precision_values)}

# Extend recall_values to include traditional steps for a better curve (0.1, 0.2 ...)
recall_values.extend(
    [step for step in np.arange(0.0, 1.1, 0.2) if step not in recall_values]
)
recall_values = sorted(set(recall_values))

# Extend matching dict to include these new intermediate steps
for idx, step in enumerate(recall_values):
    if step not in precision_recall_match:
        if idx > 0 and recall_values[idx - 1] in precision_recall_match:
            precision_recall_match[step] = precision_recall_match[
                recall_values[idx - 1]
            ]
        else:
            precision_recall_match[step] = precision_recall_match[
                recall_values[idx + 1]
            ]

disp = PrecisionRecallDisplay(
    [precision_recall_match.get(r) for r in recall_values], recall_values
)
disp.plot(ax=ax, name="Boosted", color="darkorange")

plt.ylim((0, 1.1))
plt.savefig("precision_recall_graph.png")