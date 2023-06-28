"""This module performs textual analysis on the dataset text"""
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

df = pd.read_csv("data/spacenews_final.csv")
TITLES = " ".join(cat for cat in df.title)
CONTENTS = " ".join(cat for cat in df.content)
TEXT = TITLES + CONTENTS

# Creating the text variable
stop_words = ["will", "said"] + list(STOPWORDS)

# Generate word cloud
word_cloud = WordCloud(
    width=3000,
    height=2000,
    random_state=1,
    background_color="black",
    colormap="Pastel1",
    collocations=False,
    min_word_length=2,
    normalize_plurals=True,
    include_numbers=False,
    stopwords=stop_words,
).generate(TEXT)

# Display the generated Word Cloud
plt.imshow(word_cloud)
plt.axis("off")
plt.show()
