import requests

api_url = "https://api.dictionaryapi.dev/api/v2/entries/en/"

word = "hello"

response = requests.get(api_url + word)

if response.status_code == 200:
    data = response.json()
    print("GET REQUEST SUCCESSFUL")
    print(data[0]["word"])
else:
    print("GET REQUEST FAILED with status code: {response.status_code}")
