import requests
from requests.auth import HTTPBasicAuth

# Define API credentials (example)
username = "admin"
password = "password123"

# Base URL for the API
BASE_URL = "https://restful-booker.herokuapp.com"

# Authentication header (using HTTPBasicAuth)
auth = HTTPBasicAuth(username, password)

# Define the endpoint for fetching token (if applicable)
token_endpoint = f"{BASE_URL}/auth"

# Make the request to the auth endpoint
response = requests.post(token_endpoint, auth=auth)

# Check if the request was successful and extract the token
if response.status_code == 200:
    token_data = response.json()
    token = token_data.get('token')  # Assuming the token is in 'token' field
    print(f"Fetched Token: {token}")
else:
    print(f"Failed to fetch token. Status Code: {response.status_code}, Response: {response.text}")