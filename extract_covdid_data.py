import requests
import yaml
from dotenv import load_dotenv
import os

# load the api url from a .env
load_dotenv()
url = os.getenv("WEATHER_API")
api_key = os.getenv("RAPID_API_KEY")
api_host = os.getenv("RAPID_API_HOST")

# query params for the api call
querystring = {"q": "Quito"}

# headers from rapid api
headers = {
    "X-RapidAPI-Key": api_key,
    "X-RapidAPI-Host": api_host,
}

# make the api call
response = requests.get(url, headers=headers, params=querystring)

# format the data
data = response.json()
del data["current"]["condition"]
formatted_data = {**data["current"], **data["location"]}

# display the data in a yaml format for a better reading
print(yaml.dump(formatted_data, allow_unicode=True, default_flow_style=False))
