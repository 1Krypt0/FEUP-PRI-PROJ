"""Cleans the data retrieved from the Spacenews dataset."""

import pandas as pd

news = pd.read_csv("data/spacenews_filled.csv")

# Drop post excerpt column
news.drop("postexcerpt", axis=1, inplace=True)

# Remove articles that had no corresponding content online
news.dropna(inplace=True)

news.to_csv("data/spacenews_clean.csv", index=False)
