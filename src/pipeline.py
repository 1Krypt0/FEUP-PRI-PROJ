import pandas as pd
import numpy as np
from newspaper import Article, ArticleException
from sqlalchemy.sql import False_

news = pd.read_csv('data/spacenews.csv')

# Find out where there is no content
empty_content = np.asarray(np.where(pd.isnull(news['content'])))[0]

urls = news['url'][empty_content]

# Parse the original article and fill up the rest of the table
for url, index in zip(urls, empty_content):
    article = Article(url)
    try:
        article.download()
        article.parse()
    except ArticleException as exception:
        print(f"Could not find article relative to URL {url}. Index was {index}")
        continue
    news['content'][index] = article.text.replace('\n', ' ')
    print(f"Parsed news item {index}")

# Drop post excerpt column
news.drop("postexcerpt", axis=1, inplace=True)

# Remove articles that had no corresponding content online
news.dropna(inplace=True)

# Remove authors from this dataset and add it into another
authors = news['author']
authors = authors.unique()
authors = pd.DataFrame(authors)
authors.columns = ['name']

for index, author in zip(authors.index, authors['name']):
    articles = news.index[news['author'] == author].tolist()
    news['author'][articles] = index

authors.to_csv('data/authors.csv')
news.rename(columns = {'author': 'authorID'}, inplace=True)
news.to_csv('data/spacenews_clean.csv', index=False)

# Without this section this doesn't work, for some reason

clean_news = pd.read_csv('data/spacenews_clean.csv')

# Remove articles that had no corresponding content online
clean_news.dropna(inplace=True)

clean_news.to_csv('data/spacenews_clean.csv')
