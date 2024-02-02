import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(url=URL)
data = response.text
soup = BeautifulSoup(data, "html.parser")
# print(soup.prettify())
title_list = soup.find_all(name="h3", class_="title")
movie_list = []
for title in title_list:
    movie_list.append(title.getText())

print(movie_list)
with open("movie.txt", mode="w", encoding="utf-8") as movies:
    for x in range(101):
        number = x - (x + x)
        if number < 0:
            movies.write(f"{movie_list[number]}\n")


    # movies.write()



