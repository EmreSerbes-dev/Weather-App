import requests
from pprint import pprint

import urllib.parse

address = 'Shivaji Nagar, Bangalore, KA 560001'

url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) +'?format=json'

loc = requests.get(url).json()
print(loc[0]["lat"])
print(loc[0]["lon"])

API= "your api code here"


base = "https://api.openweathermap.org/data/3.0/onecall?lat=" + loc[0]["lat"] + "&lon="+ loc[0]["lon"] + "&appid=" + API

wData = requests.get(base).json()

pprint(wData)
