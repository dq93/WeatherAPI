import requests
import pandas as pd
from bs4 import BeautifulSoup
import json
import csv

URL = 'https://historical-forecast-api.open-meteo.com/v1/forecast?latitude=-21.72&longitude=-45.39&start_date=2022-01-01&end_date=2023-12-31&hourly=temperature_2m,relative_humidity_2m,precipitation,surface_pressure'

response = requests.get(URL)
data = response.json()

output = 'data/json/weather_data.json'

with open(output, 'w') as f:
    json.dump(data, f, indent=4)

#CSV_PATH = 'data/CSV/weather_data.csv'