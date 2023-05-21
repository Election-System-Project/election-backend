import requests

endpoint = "http://localhost:8000/announcementController/"
data = {
    "title": "hiiii",
    "content": "Mhelloo",
    "announcement_type": "result"
}

response = requests.post(endpoint, json=data)

print(response.json())