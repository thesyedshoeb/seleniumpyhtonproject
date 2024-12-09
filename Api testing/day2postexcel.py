import requests
import pytest
import pandas as pd

# Base URL for the API
BASE_URL = "https://restful-booker.herokuapp.com"

EXCELPATH = r"C:\Users\shoeb.syed\Downloads\excelread.xlsx"

def get_payloads_from_excel(file_path):
    """Read payloads from an Excel file."""
    data = pd.read_excel(file_path)
    payloads = []
    for _, row in data.iterrows():
        # Convert row to dictionary and appropriate types
        payload = {
            "firstname": row["firstname"],
            "lastname": row["lastname"],
            "totalprice": int(row["totalprice"]),
            "depositpaid": row["depositpaid"] in [True, "True", 1],
            "bookingdates": {
            "checkin": row["checkin"],
            "checkout": row["checkout"]
            },
            "additionalneeds": row["additionalneeds"]
        }
        payloads.append(payload)
    return payloads


@pytest.mark.parametrize("payload", get_payloads_from_excel(EXCELPATH))
def test_create_booking(payload):
    """Test case to create a booking using data from Excel."""
    # --- Step 1: Create a Booking ---
    create_endpoint = f"{BASE_URL}/booking"

    create_headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    # Perform POST request
    create_response = requests.post(create_endpoint, headers=create_headers, json=payload)

    # Validate POST response
    assert create_response.status_code == 200, "Failed to create booking"
    booking_data = create_response.json()
    booking_id = booking_data.get("bookingid")
    print(f"Created Booking ID: {booking_id}")

