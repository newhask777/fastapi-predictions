import requests
import json

url = "https://football-prediction-api.p.rapidapi.com/api/v2/away-last-10/253300"

headers = {
	"X-RapidAPI-Key": "7ca9a3c5c9mshef5b48845d7690ep19e04bjsn6041fa46a9c8",
	"X-RapidAPI-Host": "football-prediction-api.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

with open('Football Prediction/json/al10.json', 'w', encoding='utf-8') as f:
    json.dump(response.json(), f, indent=4, ensure_ascii=False)

print(response.json())