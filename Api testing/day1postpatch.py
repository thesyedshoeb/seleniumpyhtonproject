import requests
import pytest

# Base URL for the API
BASE_URL = "https://restful-booker.herokuapp.com"


def test_create_and_update_booking():
    """Test case to create a booking and then update it."""

    # --- Step 1: Create a Booking ---
    create_endpoint = f"{BASE_URL}/booking"
    create_payload = {
        "firstname": "John",
        "lastname": "Doe",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-12-01",
            "checkout": "2024-12-10"
        },
        "additionalneeds": "Breakfast"
    }

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
    print(f"Created Booking ID: {booking_id}")

    # --- Step 2: Update the Created Booking ---
    update_endpoint = f"{BASE_URL}/booking/{booking_id}"
    update_payload = {
        "firstname": "shoeb",
        "lastname": "syed",
    }

    # Add Authorization Header for PUT request
    update_headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": "Basic YWRtaW46cGFzc3dvcmQxMjM="  # Replace with valid credentials
    }

    # Perform PUT request
    update_response = requests.patch(update_endpoint, headers=update_headers, json=update_payload)

    # Validate PUT response
    assert update_response.status_code == 200, "Failed to update booking"
    updated_data = update_response.json()
    print(f"Updated Booking Data: {updated_data}")
