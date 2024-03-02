#-- Active: 1709085540705@@redis-18411.c251.east-us-mz.azure.cloud.redislabs.com@18411

#API FROM <https://rapidapi.com/amrelrafie/api/movies-tv-shows-database>

import requests
from requests import Session
import api_key
import json
import redis
#from db_config import get_redis_connection, get_mysql_connection

# CONNECT TO REDIS DATABASE
redis_host = 'localhost'
redis_port = 6379

def redis_string():
    try:
        r = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)
        r.set("message", "Hello, world!")
        msg = r.get("message")
        print(msg)
    except Exception as e:
        print(e)
 #   r = redis.StrictRedis(host='redis-18411.c251.east-us-mz.azure.cloud.redislabs.com', port=18411, db=1)
 #   your_json = json.loads(your_json)

redis_string()





# BRINGING IN API

# CREATING A CLASS
class CMC:
    def __init__(self,token):
        self.apiurl = 'https://movies-tv-shows-database.p.rapidapi.com/'
        self.headers = {'Accepts': 'applications/json', 'X-CMC_PRO_API_KEY': token,}
        self.session = Session()
        self.session.headers.update(self.headers)

cmc = CMC(api_key.API_KEY)
cmc.apiurl


url = "https://movies-tv-shows-database.p.rapidapi.com/"
querystring = {"movieid":"tt1375666"}
headers = {
	"Type": "get-movie-details",
	"X-RapidAPI-Key": api_key.API_KEY, # "25bc92d2c8msh7d2e87cd575cceap1a336ajsnaca79d76c2c2",
	"X-RapidAPI-Host": "movies-tv-shows-database.p.rapidapi.com"
}

# REQUESTING INFO FROM API
response = requests.get(url, headers=headers, params=querystring)
#print(response.json())

# CHECK IF REQUEST WAS SUCCESSFUL (status code 200)
if response.status_code == 200:
    
    # PARSING JSON DATA
    data = response.json()

    # QUERY BY TITLE
    querystring = {"title":"Harry Potter"}

    headers = {
        "Type": "get-movies-by-title",
        "X-RapidAPI-Key": "25bc92d2c8msh7d2e87cd575cceap1a336ajsnaca79d76c2c2",
        "X-RapidAPI-Host": "movies-tv-shows-database.p.rapidapi.com"
    }

# LOADS FILE AND INDENTS IT FOR EASIER READING
    response = requests.get(url, headers=headers, params=querystring)
    with open('movie_data.json', 'w') as json_file:
        json.dump(response.json(), json_file, indent=4)

 # reads the file in terminal
    with open('movie_data.json', 'r') as json_file:
         data = json.load(json_file)
         #print(data)

