import pytest
import requests
import json

# Base URL for the API
BASE_URL = "https://restful-booker.herokuapp.com"

def test_create_booking():
    """Test case to perform a POST request to /booking with headers."""
    endpoint = f"{BASE_URL}/booking"

    # Headers for the request
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    # Load payload from the JSON file
    with open('payload.json', 'r') as file:
        payload = json.load(file)

    # Perform POST request with headers and payload
    response = requests.post(endpoint, headers=headers, json=payload)

    # Log the status code for debugging
    print(f"Status Code: {response.status_code}")

    # Assert the status code is 201 (created)
    assert response.status_code == 200, f"Expected status code 201, but got {response.status_code}"

    # Log the response content for debugging
    print(f"Response Body: {response.text}")