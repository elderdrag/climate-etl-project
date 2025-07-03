import requests
import pandas as pd
from sqlalchemy import create_engine

url = "https://api.open-meteo.com/v1/forecast?latitude=43.6047&longitude=1.4442&current_weather=true"
response = requests.get(url)
data = response.json()

weather_data = {"temp": [data['current_weather']['temperature']], "windspeed": [data['current_weather']['windspeed']],
    "time": [data['current_weather']['time']]
}
df_weather = pd.DataFrame(weather_data)


engine = create_engine('sqlite:///climate_data.db')
df_weather.to_sql('weather', con=engine, if_exists='append', index=False)
print ("Data saved successfully")

df = pd.read_sql('SELECT * FROM weather', engine)
print(df)
