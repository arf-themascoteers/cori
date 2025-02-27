import requests
import matplotlib.pyplot as plt
from datetime import datetime

# API endpoint and parameters
url = "https://archive-api.open-meteo.com/v1/archive"
params = {
    "latitude": 35.6895,
    "longitude": 139.6917,
    "start_date": "2024-01-01",
    "end_date": "2024-01-07",
    "daily": "temperature_2m_max"
}

# Fetch data from the API
response = requests.get(url, params=params)
data = response.json()

# Extract dates and maximum temperatures
dates = data['daily']['time']
max_temperatures = data['daily']['temperature_2m_max']

# Convert date strings to datetime objects for plotting
dates = [datetime.strptime(date, "%Y-%m-%d") for date in dates]

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(dates, max_temperatures, marker='o', linestyle='-', color='b')
plt.title('Daily Maximum Temperatures in Tokyo (Jan 1 - Jan 7, 2024)')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
