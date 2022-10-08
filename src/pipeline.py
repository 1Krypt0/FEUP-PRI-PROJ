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

# Remove authors from this dataset and add it into another
authors = df["author"]
authors = authors.unique()
authors = pd.DataFrame(authors)
authors.columns = ['name']

for index, author in zip(authors.index, authors['name']):
    articles = df.index[df['author'] == author].tolist()
    df['author'][articles] = index


authors.to_csv('data/authors.csv')
df.rename(columns = {'author': 'authorID'}, inplace=True)
df.to_csv('data/spacenews_clean.csv')
