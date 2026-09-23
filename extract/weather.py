import requests
import pandas as pd

CLIMATE_URL = "https://climate-api.open-meteo.com/v1/climate"
FLOOD_URL = "https://flood-api.open-meteo.com/v1/flood"

cities = {
    "Stockholm": (59.3293, 18.0686),
    "Gothenburg": (57.7089, 11.9746),
    "Malmo": (55.6050, 13.0038),
    "Uppsala": (59.8586, 17.6389),
    "Kiruna": (67.8558, 20.2253),
}


def get_climate_data(city, latitude, longitude):
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "start_date": "2020-01-01",
        "end_date": "2050-01-01",
        "models": "EC_Earth3P_HR",
        "daily": (
            "temperature_2m_mean,"
            "temperature_2m_max,"
            "temperature_2m_min,"
            "precipitation_sum"
        ),
        "timezone": "Europe/Stockholm",
    }
    print("About to requets...")
    response = requests.get(CLIMATE_URL, params=params, timeout=30)
    print("Got response:", response.status_code)
    response.raise_for_status()  

    data = response.json()
    df = pd.DataFrame(data["daily"])
    df["city"] = city
    df["latitude"] = latitude
    df["longitude"] = longitude
    return df


def get_flood_data(city, latitude, longitude):
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "start_date": "2020-01-01",
        "end_date": "2024-12-31",
        "daily": "river_discharge",
        "timezone": "Europe/Stockholm",
    }
    print("About to request...")
    response = requests.get(FLOOD_URL, params=params, timeout=30)
    print("Got response", response.status_code)
    response.raise_for_status()

    data = response.json()
    df = pd.DataFrame(data["daily"])
    df["city"] = city
    df["latitude"] = latitude
    df["longitude"] = longitude
    return df


if __name__ == "__main__":
    city, (lat, lon) = "Stockholm", cities["Stockholm"]

    print("Climate:")
    print(get_climate_data(city, lat, lon).head())

    print("\nFlood:")
    print(get_flood_data(city, lat, lon).head())