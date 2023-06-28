""" Parses the Spacenews website to fill in missing information in the dataset.

    Uses the newspaper library to fetch the missing articles from the dataset
    and fills them in, in the content column. If no article is available, it
    is skipped. Re-saves the csv file when all is done.
"""


import pandas as pd
import numpy as np
from newspaper import Article, ArticleException

news = pd.read_csv("data/spacenews.csv")

# Find out where there is no content
empty_content = np.asarray(np.where(pd.isnull(news["content"])))[0]

urls = news["url"][empty_content]

# Parse the original article and fill up the rest of the table
for url, index in zip(urls, empty_content):
    article = Article(url)
    try:
        article.download()
        article.parse()
    except ArticleException as exception:
        print(f"Could not find article relative to URL {url}. Index was {index}")
        continue
    news["content"][index] = article.text.replace("\n", " ")
    print(f"Parsed news item {index}")

news.to_csv("data/spacenews_filled.csv", index=False)
