"""Module that scrapes an article to get the sections and tags"""

from urllib.parse import urlparse
from bs4 import BeautifulSoup as bs, NavigableString
import requests


def extract_tags_sections(url):
    """Function that returns a dict with the tags and sections of the article in the url"""
    tags = []
    sections = []
    page_html = requests.get(url, timeout=3).content
    soup = bs(page_html, "lxml")

    container = soup.find("div", attrs={"class": "tax-container"})

    for element in container:

        # Ignore NavigableStrings (can't be parsed)
        if isinstance(element, NavigableString):
            continue

        href = element.get("href")
        parsed_path = list(filter(None, urlparse(href).path.split("/")))

        if parsed_path[0] == "tag":
            tags.append(parsed_path[1])
        elif parsed_path[0] in {"section", "special-feature"}:
            sections.append(parsed_path[1])
        else:
            print("unexpected: " + parsed_path[0])

    return {"tags": tags, "sections": sections}
