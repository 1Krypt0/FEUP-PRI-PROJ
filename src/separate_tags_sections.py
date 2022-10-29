import pandas as pd

news = pd.read_csv("data/spacenews_final.csv")
news.rename(columns={"Unnamed: 0": "articleID"}, inplace=True)


tags_articles = pd.concat([news["articleID"], news["tags"]], axis=1)

tags_data = []

for articleID, tags in zip(tags_articles["articleID"], tags_articles["tags"]):
    try:
        parsed_tags = tags.replace("[", "").replace("]", "").replace("'", "").split(",")
    except AttributeError:
        parsed_tags = []
        pass
    for pt in parsed_tags:
        tags_data.append([articleID, pt])

final = pd.DataFrame(tags_data, columns=["articleID", "tag"])
print(final)
