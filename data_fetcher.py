import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

ANIMALS_URL = "https://api.api-ninjas.com/v1/animals"


def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary
    """
    params = {"name": animal_name}
    headers = {"X-Api-Key": API_KEY}

    request = requests.get(ANIMALS_URL, params=params, headers=headers)
    response = request.json()
    return response
