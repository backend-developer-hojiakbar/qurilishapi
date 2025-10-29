import requests
import json

# Test the login endpoint
url = "http://127.0.0.1:8000/api/users/login/"
data = {
    "token": "test-token-123"
}

response = requests.post(url, json=data)
print(f"Status Code: {response.status_code}")
print(f"Response: {response.json()}")