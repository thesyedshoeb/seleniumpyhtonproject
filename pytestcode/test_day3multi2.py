import json
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


# Load data from the JSON file
def load_test_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


# Define the driver fixture
@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)  # Keep the browser open after test finishes
    service = Service('C:\\Users\\shoeb.syed\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=service)
    driver.implicitly_wait(5)

    # Maximize window and return the driver
    driver.maximize_window()
    yield driver  # This will pass the driver to the test function
    driver.quit()  # Cleanup: quit the driver after the test


# Test login functionality
def test_login(driver):
    # Load test data from JSON
    test_data = load_test_data("multijson.json")
    print(test_data)

    for data in test_data:
        driver.get(data["url"])  # Use the URL from test data
        time.sleep(2)  # Let the page load

        # Locate username and password fields (update selectors as per your app)
        username_field = driver.find_element("name", "username")  # Replace with actual ID/selector
        password_field = driver.find_element("name", "password")  # Replace with actual ID/selector

        # Enter credentials
        username_field.clear()
        username_field.send_keys(data['username'])
        password_field.clear()
        password_field.send_keys(data['password'])

        # Submit the form
        driver.find_element("xpath", "//button[@type='submit']").click()
        time.sleep(3)  # Wait for response

        # Verify login result (customize as per app, e.g., check for error message or dashboard)
        # if "dashboard" in driver.current_url:  # Replace with actual condition
        #     print(f"Login successful for {data['username']}")
        # else:
        #     print(f"Login failed for {data['username']}")
