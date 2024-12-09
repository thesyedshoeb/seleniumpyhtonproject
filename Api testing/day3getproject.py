import pytest
import requests
import json

# Base URL for the API
BASE_URL = "https://gorest.co.in/public/v2"

def test_post_booking():
    """Test case to perform a POST request to /booking with headers."""
    endpoint = f"{BASE_URL}/users/7567112"

    # Headers for the request
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": "Bearer 49afb799cbe1e2a91ca7905d57228fd22e9941ea88bddf1b0f63b8d0cf8354cf"
    }

    # Sample data to be sent in the POST request
    '''payload = {"id":180968,
               "user_id":7566987,
               "title":"Amplus denego voco alter speciosus.",
               "body":"Cattus labore tutamen. Dolorum advenio quidem. Calculus admitto coadunatio. Avoco vereor vomica. Voluptatem quia vapulus. Caries ducimus thesis. Admoneo cicuta voluptatum. Thermae ait temptatio. Aut tersus ullam. Deinde dedico cunabula. Aestas pecto vero. Attollo contra quasi. Amissio commemoro occaecati. Apto adficio attollo. Qui cur sordeo."}'''
    # Perform POST request with headers
    #response = requests.get(endpoint, headers=headers, json=payload)
    response = requests.get(endpoint, headers=headers)


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
