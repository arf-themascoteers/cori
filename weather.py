import requests

def get_weather():
    url = f"https://geocoding-api.open-meteo.com/v1/search?name=Melbourne&count=1"
    response = requests.get(url).json()

    lat = response["results"][0]["latitude"]
    lon = response["results"][0]["longitude"]
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m"
    weather_response = requests.get(weather_url).json()
    return {"city": city, "temperature": weather_response["current"]["temperature_2m"]}

print(get_weather())