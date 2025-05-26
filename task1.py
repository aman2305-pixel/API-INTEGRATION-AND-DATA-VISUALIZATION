import requests
import matplotlib.pyplot as plt

API_KEY = 'your_openweathermap_api_key'
CITY = 'Mumbai'
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)
data = response.json()

dates = [item['dt_txt'] for item in data['list'][:8]]
temps = [item['main']['temp'] for item in data['list'][:8]]

plt.figure(figsize=(10,5))
plt.plot(dates, temps, marker='o')
plt.title(f'Temperature Forecast for {CITY}')
plt.xlabel('Date & Time')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True)
plt.show()
