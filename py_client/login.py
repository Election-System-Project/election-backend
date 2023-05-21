import requests

endpoint = "http://localhost:8000/authcontroller/login/"

data = {
    "username": "malikhinnawi01@gmail.com",
    "password": "Mnk7219@2001"
}

response = requests.post(endpoint, json=data)

print(response.json())