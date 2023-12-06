import requests
import yaml

url = "https://weatherapi-com.p.rapidapi.com/current.json"

querystring = {"q": "Quito"}

headers = {
    "X-RapidAPI-Key": "bcbb788ef0mshb53c3476f943474p16c6f0jsn240dd883d47c",
    "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com",
}

response = requests.get(url, headers=headers, params=querystring)

data = response.json()
del data["current"]["condition"]
formatted_data = {**data["current"], **data["location"]}

print("normal", formatted_data)
print(yaml.dump(formatted_data, allow_unicode=True, default_flow_style=False))
