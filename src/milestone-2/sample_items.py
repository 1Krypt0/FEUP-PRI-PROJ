import random
import pandas as pd

articles = pd.read_json("./solr/spacenews_better.json")

new_articles = articles.sample(n=15)


new_articles.to_json("temp.json", orient="records")
