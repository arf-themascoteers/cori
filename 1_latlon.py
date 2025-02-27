import requests

url = f"https://geocoding-api.open-meteo.com/v1/search?name=Melbourne&count=1"
response = requests.get(url).json()
print(response)
lat = response["results"][0]["latitude"]
lon = response["results"][0]["longitude"]
print(lat)
print(lon)