import requests
import pandas as pd
import json

URL = "https://historical-forecast-api.open-meteo.com/v1/forecast?latitude=-21.72&longitude=-45.39&start_date=2022-01-01&end_date=2023-12-31&hourly=temperature_2m,relative_humidity_2m,precipitation,surface_pressure"

response = requests.get(URL)

if response.status_code == 200:
    
    data = response.json()

    json_data_filepath = "data/json/weather_data.json"

    with open(json_data_filepath, "w") as file:
        json.dump(data, file, indent=4)
    
    df = pd.DataFrame(data)

    hourly_data = pd.DataFrame(data["hourly"])

    cleaned_data = hourly_data[["time", "temperature_2m", "relative_humidity_2m", "precipitation", "surface_pressure"]]

    new_df = pd.DataFrame(cleaned_data)

    csv_filepath = "data/csv/weather_data.csv"

    new_df.to_csv(csv_filepath, index=False)
    
else:
    print("error unable to access")
