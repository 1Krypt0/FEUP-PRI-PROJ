import pandas as pd
import numpy as np
from newspaper import Article

df = pd.read_csv('data/spacenews.csv')

# Find out where there is no content
empty_content = np.asarray( np.where(pd.isnull(df["content"])))[0]

urls = df["url"][empty_content]

# Parse the original article and fill up the rest of the table
for url, index in zip(urls, empty_content):
    article = Article(url)
    article.download()
    article.parse()
    df["content"][index] = article.text.replace('\n', ' ')
    print(f"Parsed news item {index}")

df.to_csv('data/spacenews_filled.csv')


