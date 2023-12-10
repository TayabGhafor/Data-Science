# 18-09-2023
# CSC461 – Assignment1 – Web Scraping
# Muhammad Tayab
# Fa21-bse-030

import requests
from bs4 import BeautifulSoup
import time
import csv

# Creating list of URLs
Movie_Urls = [
"https://www.imdb.com/title/tt0133093/", # The Matrix
"https://www.imdb.com/title/tt9362722/", # Spider-Man: Across the Spider-Verse
"https://www.imdb.com/title/tt0071562/", # The Dark Knight
"https://www.imdb.com/title/tt1187043/", # 3 Idiots
"https://www.imdb.com/title/tt1201607/", # Harry Potter and the Deathly Hallows
]

# Creating list to store data
Movie_Data = []

# using for loop on URLs to get information
for movie_url in Movie_Urls:

    response = requests.get(movie_url)

    # Checking request status
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")

        # Extracting movie titles & ratings
        movie_title = soup.find("h1", itemprop="name").text
        movie_rating = soup.find("span", itemprop="ratingValue").text

        # Adding data to list
        Movie_Data.append([movie_title, movie_rating])

    # Sleep for 1 second
    time.sleep(1)

# Exporting data to Excel file
with open("favorite_movies.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Title", "Rating"])
    for movie in Movie_Data:
        writer.writerow(movie)
