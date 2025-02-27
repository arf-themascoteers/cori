import requests

weather_url = f"https://api.open-meteo.com/v1/forecast?latitude=-37.814&longitude=144.96332&current=temperature_2m"
weather_response = requests.get(weather_url).json()
current = weather_response["current"]
temp = current["temperature_2m"]
print(temp)
