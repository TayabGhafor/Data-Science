# 12-03-2024
# CSC461 – Assignment1 – Web Scraping
# Muhammad Tayab
# Fa21-bse-030

# Question_1

import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of Movies
url = 'https://www.imdb.com/chart/top/'

# Sending request
response = requests.get(url)

# Parsing the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Finding all movie rows in the table
movie_rows = soup.find_all('tr')

# Initializing lists to store data
titles = []
years = []
durations = []
ratings = []

# Iterating over each movie row
for row in movie_rows[1:]:  
    # Extracting movie title
    title = row.find('td', class_='titleColumn').find('a').text
    titles.append(title)
    
    # Extracting movie year
    year = row.find('span', class_='secondaryInfo').text.strip('()')
    years.append(year)
    
    # Extracting movie duration
    duration = row.find('span', class_='runtime').text.strip()
    durations.append(duration)
    
    # Extracting movie rating
    rating = row.find('td', class_='ratingColumn imdbRating').find('strong').text
    ratings.append(rating)

# Creating DataFrame to store data
movie_data = pd.DataFrame({
    'Title': titles,
    'Year': years,
    'Duration': durations,
    'IMDB Rating': ratings
})

# Exporting data to CSV
movie_data.to_csv('imdb_top_250_movies.csv', index=False)


# Question_2

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://space-facts.com/mars/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

# Findind Mars table data
table = soup.find('table', class_='tablepress tablepress-id-p-mars')

# Extracting table rows
rows = table.find_all('tr')

# Initializing lists to store data
labels = []
values = []

# Iterate over each row
for row in rows:
    # Extracting label and value
    label = row.find('td', class_='column-1').text.strip()
    value = row.find('td', class_='column-2').text.strip()
    
    # Appending label and value to lists
    labels.append(label)
    values.append(value)

# Create a DataFrame to store the Mars data
mars_profile = pd.DataFrame({
    'Label': labels,
    'Value': values
})

# Export data to Excel
mars_profile.to_excel('mars_planet_profile.xlsx', index=False)
