import os
import sys
import requests

API_URL = "http://localhost:8080"
API_KEY = os.environ.get("API_KEY")

response = requests.post(API_URL, headers={"X-Api-Key": API_KEY})

if response.status_code == 200:
    print("You did it, yay!", file=sys.stderr)
else:
    print(f"Got an invalid status code {response.status_code}", file=sys.stderr)
    sys.exit(1)
