
# March 29, 2024
# CSC461 – Assignment2 – IDS – Data Visualization
# Muhammad Tayab
# FA21-BSE-030
# five questions are given and their datasets are also provided at the drive.
# we have to load the dataset and visualize the data ont he charts.

'''
Question1:
The world population dataset provides population data from 1960 to 2020 for countries around the world.
Compare the populations of top 10 highest populated countries (in 2020) over the entire period using a chart.
Make appropriate modifications to the chart title, axis titles, legend, figure size, font size, colors etc. to make
the chart readable and visually appealing.
'''

import pandas as pd
import matplotlib.pyplot as plt
from google.colab import drive

# Mounting Drive
drive.mount('/content/drive')

# Path to CSV file
file_path = '/content/drive/MyDrive/IDS/datasets/datasets/world_pop.csv'

# Loading dataset
data = pd.read_csv(file_path)

# Extracting country names
countries = data['country'].tolist()

# Filtering data for the top 10 most populous countries in 2020
top_10_countries_2020 = data.sort_values(by='year_2020', ascending=False).head(10)

# Filtering data for the top 10 countries over the entire period
top_10_data = data[data['country'].isin(top_10_countries_2020['country'])]

# Plotting
plt.figure(figsize=(12, 8))

for country in top_10_countries_2020['country']:
    country_data = top_10_data[top_10_data['country'] == country]
    plt.plot(country_data.columns[1:], country_data.iloc[0, 1:], label=country)

plt.title('Population Trends of Top 10 Most Populous Countries (1960-2020)', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Population', fontsize=14)
plt.xticks(rotation=45, fontsize=12)
plt.yticks(fontsize=12)
plt.legend(loc='upper left', fontsize=12)
plt.grid(True)
plt.tight_layout()
plt.show()

'''
Question2:
Using the world population dataset (from Q1)
• Show the population of 10 least populous countries in 2015 using a chart.
• Calculate the change in population of Pakistan, India, United States, and United Kingdom from 1970
to 2010 and show the population change (in millions) using a chart.
• Calculate the Pakistan population growth between 2010-2020 and then show the data using a chart.
'''

# Part 1: Population of 10 least populous countries in 2015
least_populous_2015 = data.sort_values(by='year_2015').head(10)
plt.figure(figsize=(10, 6))
plt.barh(least_populous_2015['country'], least_populous_2015['year_2015'])
plt.xlabel('Population')
plt.ylabel('Country')
plt.title('Population of 10 Least Populous Countries in 2015')
plt.gca().invert_yaxis()  # Invert y-axis to have the highest population at the top
plt.show()

# Part 2: Population change from 1970 to 2010 for Pakistan, India, United States, and United Kingdom
countries = ['Pakistan', 'India', 'United States', 'United Kingdom']
pop_change = data[data['country'].isin(countries)]
pop_change = pop_change[['country', 'year_1970', 'year_2010']].set_index('country')
pop_change['change'] = (pop_change['year_2010'] - pop_change['year_1970']) / 10**6  
# Convert to millions
plt.figure(figsize=(10, 6))
plt.bar(pop_change.index, pop_change['change'])
plt.xlabel('Country')
plt.ylabel('Population Change (Millions)')
plt.title('Population Change from 1970 to 2010')
plt.show()

# Part 3: Pakistan population growth between 2010-2020
pakistan_growth = data[data['country'] == 'Pakistan']
pakistan_growth = pakistan_growth[['country', 'year_2010', 'year_2020']]
pakistan_growth['growth'] = (pakistan_growth['year_2020'] - pakistan_growth['year_2010']) / 10**6  
# Convert to millions
plt.figure(figsize=(10, 6))
plt.plot(pakistan_growth.columns[1:], pakistan_growth.iloc[0, 1:], marker='o')
plt.xlabel('Year')
plt.ylabel('Population Growth (Millions)')
plt.title('Pakistan Population Growth (2010-2020)')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

'''
Question3:
The diamonds dataset contains 53,000 records with various attributes like carat, cut, color, clarity, price etc.
Plot the relationship between ‘carat’ and ‘price’ of diamonds using a chart. Because it’s a large dataset, just
plot the diamonds with a ‘clarify’ = ‘SI2’ and ‘color’ = ‘E’. Use the values of the ‘cut’ for colors in the plot.
Make appropriate modifications to the chart title, axis titles, legend, figure size, font size, colors etc. to make
the chart readable and visually appealing.
'''
# Path to CSV file 
file_path = '/content/drive/MyDrive/IDS/datasets/datasets/diamonds.csv'

# Loading the dataset
data = pd.read_csv(file_path)

#Filter diamonds with clarity = 'SI2' and color = 'E'
filtered_diamonds = data[(data['clarity'] == 'SI2') & (data['color'] == 'E')]

# Define colors for different cut values
cut_colors = {'Ideal': 'blue', 'Premium': 'green', 'Very Good': 'orange', 'Good': 'red', 'Fair': 'purple'}

# Plotting
plt.figure(figsize=(10, 6))

for cut, color in cut_colors.items():
    cut_data = filtered_diamonds[filtered_diamonds['cut'] == cut]
    plt.scatter(cut_data['carat'], cut_data['price'], label=cut, color=color, alpha=0.5)

plt.title('Relationship between Carat and Price of Diamonds (Clarity=SI2, Color=E)', fontsize=16)
plt.xlabel('Carat', fontsize=14)
plt.ylabel('Price', fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.legend(fontsize=12)
plt.grid(True)
plt.tight_layout()
plt.show()

'''
Question4:
The nuclear waste dataset contains the locations of several nuclear waste storage sites in the US. Use map of
the US to show these sites as markers on the map. Clicking on a marker should display the name of the site.
Pick the appropriate location, zoom level and images tiles for the map.
'''

import folium

# Path to CSV file 
file_path = '/content/drive/MyDrive/IDS/datasets/datasets/nuclear_waste_sites.csv'

# Loading the dataset
data = pd.read_csv(file_path)

# Creating map centered at the mean latitude and longitude of the data points
center_lat = data['lat'].mean()
center_lon = data['lon'].mean()
mymap = folium.Map(location=[center_lat, center_lon], zoom_start=5)

# Adding markers for each nuclear waste storage site
for index, row in data.iterrows():
    folium.Marker(location=[row['lat'], row['lon']], popup=row['text']).add_to(mymap)

# Displaying the map
mymap

'''
Question5:
The Pakistan heritage sites dataset contains the geo locations of a number of heritage sites across Pakistan.
Show these sites as markers on a map of the Pakistan. Clicking on a marker should display the name of the
site. Pick the appropriate location, zoom level and images tiles for the map.
'''

import folium
# Path to CSV file 
file_path = '/content/drive/MyDrive/IDS/datasets/datasets/pak-heritage-sites.csv'

# Loading the dataset
data = pd.read_csv(file_path)

# Creating map centered around Pakistan
pak_map = folium.Map(location=[30.3753, 69.3451], zoom_start=5)

# Adding markers for each heritage site
for index, row in data.iterrows():
    folium.Marker(
        location=[row['latitude'], row['longitude']],
        popup=row['site_name']
    ).add_to(pak_map)

# Displaying the map
pak_map
