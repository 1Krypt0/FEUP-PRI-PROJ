import pandas as pd

news = pd.read_csv("data/spacenews_final.csv")
news.rename(columns={"Unnamed: 0": "articleID"}, inplace=True)


tags_articles = pd.concat([news["articleID"], news["tags"]], axis=1)

sections_articles = pd.concat([news["articleID"], news["sections"]], axis=1)

tags_data = []
sections_data = []
for articleID, tags in zip(tags_articles["articleID"], tags_articles["tags"]):
    try:
        parsed_tags = tags.replace("[", "").replace("]", "").replace("'", "").split(",")
    except AttributeError:
        parsed_tags = []
        pass
    for pt in parsed_tags:
        tags_data.append([articleID, pt])

for articleID, sections in zip(
    tags_articles["articleID"], sections_articles["sections"]
):
    try:
        parsed_sections = (
            sections.replace("[", "").replace("]", "").replace("'", "").split(",")
        )
    except AttributeError:
        parsed_sections = []
        pass
    for ps in parsed_sections:
        sections_data.append([articleID, ps])


final_tags = pd.DataFrame(tags_data, columns=["articleID", "tag"])
final_sections = pd.DataFrame(sections_data, columns=["articleID", "section"])

final_tags.to_csv("data/tags.csv")
final_sections.to_csv("data/sections.csv")
