# SETUP
import matplotlib.pyplot as plt
from sklearn.metrics import PrecisionRecallDisplay
import numpy as np
import json
import requests
import pandas as pd

QRELS_FILE = "./queries/q1/qrels_mlt.txt"
QUERY_URL = "http://localhost:8983/solr/articles/select?q=Alien%20planets&q.op=AND&qf=title%5E10%20content%5E5%20tags%5E3%20sections%5E3%20author&wt=json&defType=edismax&rows=50" 
BOOSTED_QUERY_URL = "http://localhost:8983/solr/articles/mlt?defType=edismax&wt=json&q.op=OR&q=id%3Affc78d93-9331-4351-8c40-cc77f3668cd2&qf=title%5E10%20content%5E5%20tags%5E3%20sections%5E3%20author%20date%20id&rows=20"


# Read qrels to extract relevant documents
relevant = list(map(lambda el: el.strip(), open(QRELS_FILE).readlines()))
# Get query results from Solr instance
results = requests.get(QUERY_URL).json()["response"]["docs"]
boosted_results = requests.get(BOOSTED_QUERY_URL).json()["response"]["docs"]


# Define custom decorator to automatically calculate metric based on key
metrics = {}
metric = lambda f: metrics.setdefault(f.__name__, f)


@metric
def ap(results, relevant):
    """Average Precision"""
    precision_values = [
        len([doc for doc in results[:idx] if doc["title"] in relevant]) / idx
        for idx in range(1, len(results))
    ]
    return sum(precision_values) / len(precision_values)


@metric
def p10(results, relevant, n=10):
    """Precision at N"""
    return len([doc for doc in results[:n] if doc["title"] in relevant]) / n


def calculate_metric(key, results, relevant):
    return metrics[key](results, relevant)


# Define metrics to be calculated
evaluation_metrics = {"ap": "Average Precision", "p10": "Precision at 10 (P@10)"}


def calculate_metrics(results, is_boosted):
    # Calculate all metrics and export results as LaTeX table
    df = pd.DataFrame(
        [["Metric", "Value"]]
        + [
            [evaluation_metrics[m], calculate_metric(m, results, relevant)]
            for m in evaluation_metrics
        ]
    )

    name = "results2.tex"
    if is_boosted:
        name = "results2_boosted.tex"

    with open(name, "w") as tf:
        tf.write(df.to_latex())


# PRECISION-RECALL CURVE
# Calculate precision and recall values as we move down the ranked list
def calculate_pr_curve(results):
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

    return disp


calculate_metrics(results, False)
calculate_metrics(boosted_results, True)

regular = calculate_pr_curve(results)
boosted = calculate_pr_curve(boosted_results)


_, ax = plt.subplots(figsize=(5, 4))

regular.plot(ax=ax, name="Regular", color="cornflowerblue")
boosted.plot(ax=ax, name="Boosted", color="darkorange")

plt.ylim((0, 1.1))

# disp.plot()
plt.savefig("precision_recall2.pdf")
