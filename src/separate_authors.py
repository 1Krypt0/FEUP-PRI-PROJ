import pandas as pd

news = pd.read_csv("data/spacenews_clean.csv")

# Remove authors from this dataset and add it into another
authors = news["author"]
authors = authors.unique()
authors = pd.DataFrame(authors)
authors.columns = ["name"]

for index, author in zip(authors.index, authors["name"]):
    articles = news.index[news["author"] == author].tolist()
    news["author"][articles] = index

news.rename(columns={"author": "authorID"}, inplace=True)

authors.to_csv("data/authors.csv")
news.to_csv("data/spacenews_final.csv")
