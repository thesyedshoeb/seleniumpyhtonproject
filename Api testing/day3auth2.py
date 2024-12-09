import requests
from requests.auth import HTTPBasicAuth

# Define the token (usually you fetch it through a different endpoint first)
token = "your_bearer_token_here"
# Base URL for the API
BASE_URL = "https://restful-booker.herokuapp.com"

# Define the endpoint you want to access
endpoint = f"{BASE_URL}/booking"

# Make the request using the Bearer token
headers = {
    "Authorization": f"Bearer {token}"  # Bearer Token in the Authorization header
}

response = requests.get(endpoint, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    print(f"Response: {response.json()}")
else:
    print(f"Failed to fetch data. Status Code: {response.status_code}, Response: {response.text}")