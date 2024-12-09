import pytest
import requests
import json

# Base URL for the API
BASE_URL = "https://restful-booker.herokuapp.com"

def test_post_booking():
    """Test case to perform a POST request to /booking with headers."""
    endpoint = f"{BASE_URL}/booking"

    # Headers for the request
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    # Sample data to be sent in the POST request
    payload = {
        "firstname": "Shoeb",
        "lastname": "Syed",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-12-01",
            "checkout": "2024-12-10"
        },
        "additionalneeds": "Breakfast"
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
