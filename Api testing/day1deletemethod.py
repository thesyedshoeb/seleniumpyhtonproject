import pytest
import requests
import json

# Base URL for the API
BASE_URL = "https://restful-booker.herokuapp.com"

def test_update_booking():
    """Test case to perform a PUT request to /booking/{booking_id} with headers and authorization."""
    booking_id = 25  # Replace with an actual booking ID you want to update
    endpoint = f"{BASE_URL}/booking/{booking_id}"

    # Headers with Authorization
    headers = {
        "Content-Type": "application/json",  # Specify the content type
        "Accept": "application/json",  # Specify the expected response format
        "Authorization": "Basic YWRtaW46cGFzc3dvcmQxMjM="  # Replace with valid credentials
    }

    # Sample data to be sent in the PUT request (updating booking)
    '''payload = {
    "firstname" : "Shoeb",
    "lastname" : "Syed"
    }'''

    # Perform PUT request with headers
    response = requests.delete(endpoint, headers=headers)

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
