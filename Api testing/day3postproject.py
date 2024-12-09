import pytest
import requests
import json

# Base URL for the API
BASE_URL = "https://gorest.co.in/public/v2"

def test_post_booking():
    """Test case to perform a POST request to /booking with headers."""
    endpoint = f"{BASE_URL}/users"

    # Headers for the request
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": "Bearer 49afb799cbe1e2a91ca7905d57228fd22e9941ea88bddf1b0f63b8d0cf8354cf"
    }

    # Sample data to be sent in the POST request
    payload = {"id":7566330,
               "name":"Anunay Trivedi",
               "email":"shoeb@gmail.com",
               "gender":"female",
               "status":"active"
    }
    # Perform POST request with headers
    response = requests.post(endpoint, headers=headers, json=payload)

    # Log status code
    print(f"Status Code: {response.status_code}")

    # Log response content (body)
    print(f"Response Body: {response.text}")

    # Log response headers
    print(f"Response Headers: {response.headers}")

    # Optionally, you can also log JSON content if the response is in JSON format
    try:
        json_response = response.json()
        print(f"Response JSON: {json_response}")
    except ValueError:
        print("Response is not in JSON format.")
