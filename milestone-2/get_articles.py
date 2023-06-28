from datetime import datetime
import pandas as pd

articles = pd.read_json("./solr/spacenews_better.json", orient="records")

relevant = []

for i, article in articles.iterrows():
    if article["author"] == "Jeff Foust":
        date = article["date"].timestamp()
        if (
            datetime(2021, 1, 1).timestamp()
            <= date
            <= datetime(2021, 12, 31).timestamp()
        ):
            relevant.append(article["title"])

with open("test.txt", "w") as qrels:
    qrels.writelines("%s\n" % l for l in relevant)
