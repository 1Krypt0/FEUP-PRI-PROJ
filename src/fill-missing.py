import pandas as pd
import numpy as np
from newspaper import Article, ArticleException

df = pd.read_csv('data/spacenews.csv')

# Find out where there is no content
empty_content = np.asarray(np.where(pd.isnull(df["content"])))[0]

urls = df["url"][empty_content]

# Parse the original article and fill up the rest of the table
for url, index in zip(urls, empty_content):
    article = Article(url)
    try:
        article.download()
        article.parse()
    except ArticleException as exception:
        print(f"Could not find article relative to URL {url}. Index was {index}")
        continue
    df["content"][index] = article.text.replace('\n', ' ')
    print(f"Parsed news item {index}")

# Remove articles that had no corresponding content online
df.dropna()

# Drop post excerpt column
df.drop("postexcerpt", axis=1, inplace=True)

# Use spacy to extract information and keywords

df.to_csv('data/spacenews_refined.csv')
