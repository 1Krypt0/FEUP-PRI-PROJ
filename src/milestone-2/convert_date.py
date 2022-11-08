import pandas as pd

articles = pd.read_json("solr/spacenews.json")

for date, index in zip(articles["date"], articles.index):
    articles["date"][index] = date.strftime("%Y-%m-%dT%XZ")

articles.to_json("solr/spacenews_better.json", orient="records")
