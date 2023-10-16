import soupsieve
from bs4 import BeautifulSoup
import requests























# response = requests.get(url="https://news.ycombinator.com/")
# data = response.text
# soup = BeautifulSoup(data, "html.parser")
# spans = soup.find("a")
# print(spans)
# print(soup.prettify())



















# # contents = ""
# with open(file="website.html", mode="rb") as data:
#     contents = data.read()
#     # print(contents)
#
# soup = BeautifulSoup(contents, "html.parser")
# print(soup.prettify())
# all_anchor_tags = soup.find_all(name="a")
# for tags in all_anchor_tags:
#     # print(tags.getText())
#     print(tags.get("href"))
#
# heading = soup.find(name="h1", id="name")
#
# section = soup.find(name="h3", class_="heading")
# print(heading, section)
#
# embedded_anchor_tag = soup.select_one(selector="p a")
# print(embedded_anchor_tag.string)