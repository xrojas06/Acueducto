import requests
import numpy as np
from shapely.geometry import Point, Polygon

def geocode_direction(direction, api_key):
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        "address": direction,
        "key": api_key
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if data["status"] == "OK":
            # Extraer las coordenadas de latitud y longitud
            location = data["results"][0]["geometry"]["location"]
            latitude = round(location["lat"],10)
            longitude = location["lng"]
            return latitude, longitude
        else:
            print("Error en la solicitud:", data["status"])
            return None

    except Exception as e:
        print("Error:", str(e))
        return None




