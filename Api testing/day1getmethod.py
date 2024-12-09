import pytest
import requests

# Base URL for the API
BASE_URL = "https://restful-booker.herokuapp.com"

def test_get_booking():
    """Test case to perform a GET request to /booking."""
    endpoint = f"{BASE_URL}/booking"

    # Perform GET request
    response = requests.get(endpoint)

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
