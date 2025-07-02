import requests

url = "https://ai-review-backend-0iek.onrender.com/generate-review"
data = {
    "input_text": "Great battery life. Display is good. Camera is average. Sound is poor."
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Response:", response.json())

