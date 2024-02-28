import requests
import json
import redis

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

# loads the file and indents it for easy reading
    response = requests.get(url, headers=headers, params=querystring)
    with open('json_test.json', 'w') as json_file:
        json.dump(response.json(), json_file, indent=4)

# reads the file in terminal
    with open('json_test.json', 'r') as json_file:
        data = json.load(json_file)
        #print(data)

    r = redis.StrictRedis(host='redis-18411.c251.east-us-mz.azure.cloud.redislabs.com', port=18411, db=1)
    print(r)
    response = r.ping()
    if response:
        print("connected")
    else:
        print ("not connected")
    # with open('json_test.json', 'w') as data_file:
    #     test_data = json.load(response)
    # r.set('test_json', test_data)
    # print(response.json())


