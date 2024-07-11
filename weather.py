# %%
import requests
import pandas as pd
import matplotlib.pyplot as plt
import folium

# Replace with your own Visual Crossing API key
LOCATION = 'Point Reyes, CA'
BASE_URL = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline'

def get_historical_weather(location, start_date, end_date, api_key):
    url = f"{BASE_URL}/{location}/{start_date}/{end_date}?unitGroup=metric&key={api_key}&include=days"
    response = requests.get(url)
    data = response.json()
    return data['days']

# Fetch data for the past 5 years in September
# %%
years = range(2019, 2024)
weather_data = []
for year in years:
    start_date = f'{year}-09-01'
    end_date = f'{year}-09-30'
    data = get_historical_weather(LOCATION, start_date, end_date, API_KEY)
    weather_data.extend(data)

df = pd.DataFrame(weather_data)
# %%
df
# %%
# Convert to DataFrame

# Extract relevant columns
df['datetime'] = pd.to_datetime(df['datetime'])
# df = df[['datetime', 'tempmax', 'tempmin']]
# Convert Celsius to Fahrenheit
df['tempmax'] = df['tempmax'] * 9/5 + 32
df['tempmin'] = df['tempmin'] * 9/5 + 32
# %%
# Plot the data
plt.figure(figsize=(10, 5))
plt.plot(df['datetime'], df['tempmax'], label='Max Temperature (°F)', color='red')
plt.plot(df['datetime'], df['tempmin'], label='Min Temperature (°F)', color='blue')
plt.xlabel('Date')
plt.ylabel('Temperature (°F)')
plt.title('September Temperatures in Point Reyes (2019-2023)')
plt.legend()
plt.grid(True)
plt.show()


# %%
# Plot the data
plt.figure(figsize=(10, 5))
plt.bar(df['datetime'], df['precip'], color='blue')
plt.xlabel('Date')
plt.ylabel('Precipitation (inches)')
plt.title('September Rainfall in Point Reyes (2019-2023)')
plt.grid(True)
plt.show()
# %%
import requests
import pandas as pd


def get_weather_station_data(location, api_key):
    url = f"{BASE_URL}/{location}?key={api_key}&include=obs"
    response = requests.get(url)
    data = response.json()
    return data['stations']

# Get weather station data
stations = get_weather_station_data(LOCATION, API_KEY)

# Convert to DataFrame
df_stations = pd.DataFrame(stations).transpose()
df_stations = df_stations[['latitude', 'longitude', 'name']]
print(df_stations.head())
# %%
df_stations
# %% 
# Add weather stations to the map with larger icons and more prominent popups
for idx, row in df_stations.iterrows():
    folium.Marker(
        location=[row['latitude'], row['longitude']],
        popup=folium.Popup(f"<strong>{row['name']}</strong>", max_width=300),
        icon=folium.Icon(icon='star', color='red', icon_color='white', prefix='fa')
    ).add_to(m)

# Save the map to an HTML file
m.save('weather_stations_map.html')
    # %%
