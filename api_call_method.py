import requests
import json

endpoint = "https://api.openai.com/v1/completions"
API_KEY = "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"

query = "Name some travel technology companies."

payload = {
    "model": "text-davinci-003",
    "prompt": query,
    "max_tokens": 100,
    "temperature": 0.5,
}
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}",
}

response = requests.post(endpoint, headers=headers, json=payload)
print(json.dumps(response.json(), indent=3))
