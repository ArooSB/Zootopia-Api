import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_URL = "https://api.api-ninjas.com/v1/animals"

print(f"API_KEY: {API_KEY}")


def fetch_data(animal_name):
    headers = {"X-Api-Key": API_KEY}
    params = {"name": animal_name}
    response = requests.get(API_URL, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data: {response.status_code}")
        print(f"Response content: {response.text}")
        return None
