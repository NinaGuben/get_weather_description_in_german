import requests
import pandas as pd


api_key= "756d48fd3afee318c539d68224c06f23"
url = "https://openweathermap.org/"


def aktuelles_wetter(stadt):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {'appid': api_key,'q': stadt, 'units': 'metric','lang': 'de' }
    response = requests.get(url, params = params)
    if response.status_code == 200:
        data = response.json()
        print(f"Aktuelles Wetter für {stadt}\n**************************")
        wetter = data["weather"] [0] ["description"]
        print(f"Wetterlage derzeit: {wetter}")
        temp_medium = data["main"] ["temp"]
        temp_mind = data["main"] ["temp_min"]
        temp_max = data ["main"] ["temp_max"]
        print(f"Die durchschnittliche Temperatur beträgt: {temp_medium} °C  \nDie höchste Temperatur des Tages beträgt: {temp_max} °C  \nDie niedrigste Temperatur des Tages beträgt: {temp_mind} °C ")
        wind = data["wind"] ["speed"]
        print(f"Die derzeitige Wingeschwindigkeit beträgt: {wind} Meter/Sekunde")
    else:
        print("API is not accessible")

  #  print(data)


aktuelles_wetter("Wien")