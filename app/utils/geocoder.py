import os
import requests
from urllib.parse import quote_plus

API_KEY = os.getenv("GOOGLE_API_KEY")

def geocode_address(address: str, city: str):
    formatted_address = quote_plus(f"{address}, {city}")
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={formatted_address}&key={API_KEY}"
    response = requests.get(url)
    status = response.json().get('status', 'UNKNOWN_ERROR')
    if response.status_code == 200 and status == 'OK':
        results = response.json().get('results', [])
        if results:
            location = results[0].get('geometry', {}).get('location', {})
            return location.get('lat', 0), location.get('lng', 0), status
    return 0, 0, status
