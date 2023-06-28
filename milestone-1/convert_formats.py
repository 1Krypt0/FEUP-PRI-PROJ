"""
This module converts the final dataset into JSON, as it seemed easier to use for the Solr stuff
"""

import pandas as pd

news = pd.read_csv("data/spacenews_final.csv")
authors = pd.read_csv("data/authors.csv")

news.drop("Unnamed: 0", axis=1, inplace=True)

for tags, sections, index in zip(news["tags"], news["sections"], news.index):
    if pd.isna(tags):
        news["tags"][index] = []
    else:
        news["tags"][index] = (
            tags.replace("[", "").replace("]", "").replace("'", "").split(",")
        )
    if pd.isna(sections):
        news["sections"][index] = []
    else:
        news["sections"][index] = (
            sections.replace("[", "").replace("]", "").replace("'", "").split(",")
        )

for author_id, index in zip(news["authorID"], news.index):
    news["authorID"][index] = authors["name"][author_id]

news.rename(columns={"authorID": "author"}, inplace=True)

news.to_json("data/spacenews.json", orient="records")
