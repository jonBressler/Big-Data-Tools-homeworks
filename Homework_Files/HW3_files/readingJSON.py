# this is for reading the JSON from an API
import requests
import json

url = "https://movies-tv-shows-database.p.rapidapi.com/"

querystring = {"movieid":"tt1375666"}

headers = {
	"Type": "get-movie-details",
	"X-RapidAPI-Key": "25bc92d2c8msh7d2e87cd575cceap1a336ajsnaca79d76c2c2",
	"X-RapidAPI-Host": "movies-tv-shows-database.p.rapidapi.com"
}

# Make a request to the API
response = requests.get(url, headers=headers, params=querystring)

#print(response.json())

# Check if request was successful (status code 200)
if response.status_code == 200:
    # Parse JSON data
    
    data = response.json()

    # Query by Title
    querystring = {"title":"Harry Potter"}

    headers = {
        "Type": "get-movies-by-title",
        "X-RapidAPI-Key": "25bc92d2c8msh7d2e87cd575cceap1a336ajsnaca79d76c2c2",
        "X-RapidAPI-Host": "movies-tv-shows-database.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    print(response.json())

# Trying to get Title but via JSON.GET
import pandas as pd
df = pd.DataFrame(data['title'])
print(df)
