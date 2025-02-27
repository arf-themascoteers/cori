import requests
import matplotlib.pyplot as plt

url = "https://archive-api.open-meteo.com/v1/archive?latitude=35.6895&longitude=139.6917&start_date=2024-01-01&end_date=2024-01-07&daily=temperature_2m_max,temperature_2m_min"
response = requests.get(url).json()
temp = response["daily"]["temperature_2m_max"]
print(temp)
plt.plot(temp)
plt.show()