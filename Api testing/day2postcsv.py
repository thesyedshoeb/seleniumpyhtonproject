import pytest
import requests
import csv

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

    # Read payload from CSV file
    with open('csvdata.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Convert row values to appropriate types and structure the payload
            payload = {
                "firstname": row['firstname'],
                "lastname": row['lastname'],
                "totalprice": int(row['totalprice']),
                "depositpaid": row['depositpaid'] == 'True',  # Convert to boolean
                "bookingdates": {
                    "checkin": row['checkin'],
                    "checkout": row['checkout']
                },
                "additionalneeds": row['additionalneeds']
            }

            print(f"Payload before post{payload}")

            # Perform POST request with headers and payload
            response = requests.post(endpoint, headers=headers, json=payload)

            # Log the status code for debugging
            print(f"Status Code: {response.status_code}")

            # Assert the status code is 201 (created)
            assert response.status_code == 200, f"Expected status code 201, but got {response.status_code}"

            # Log the response content for debugging
            print(f"Response Body: {response.text}")

