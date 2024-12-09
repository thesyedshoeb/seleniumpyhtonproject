import requests
import pytest
import json
import allure

#command to generate report
#pytest --alluredir=reports  test_add.py
#command to run report
#allure serve reports
#to install allure
#pip install allure-pytest

# Base URL for the API
BASE_URL = "https://restful-booker.herokuapp.com"

@allure.feature("API Testing")
@allure.story("Create and Update Booking")
@allure.title("Test Case for Create and Update Booking")
@allure.description("This test case creates a booking and then updates it using payload.json")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_and_update_booking():
    """Test case to create a booking and then update it using payload.json."""

    # Load payload data from payload.json
    with open('postput.json', 'r') as file:
        payload_data = json.load(file)

    # --- Step 1: Create a Booking ---
    create_endpoint = f"{BASE_URL}/booking"
    create_payload = payload_data["create"]

    create_headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    # Perform POST request
    create_response = requests.post(create_endpoint, headers=create_headers, json=create_payload)

    # Validate POST response
    assert create_response.status_code == 200, "Failed to create booking"
    booking_data = create_response.json()
    booking_id = booking_data.get("bookingid")
    assert booking_id, "Booking ID not returned in the response"
    print(f"Created Booking ID: {booking_id}")

    # --- Step 2: Update the Created Booking ---
    update_endpoint = f"{BASE_URL}/booking/{booking_id}"
    update_payload = payload_data["update"]

    # Add Authorization Header for PUT request
    update_headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": "Basic YWRtaW46cGFzc3dvcmQxMjM="  # Replace with valid credentials
    }

    # Perform PUT request
    update_response = requests.put(update_endpoint, headers=update_headers, json=update_payload)

    # Validate PUT response
    assert update_response.status_code == 200, "Failed to update booking"
    updated_data = update_response.json()


    print(f"Updated Booking Data: {updated_data}")
