import json
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import csv

# Fixture to set up the WebDriver
@pytest.fixture()
def test_verifyURL():
    global driver
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)  # Keep the browser open after test finishes
    service = Service('C:\\Users\\shoeb.syed\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=service)
    driver.implicitly_wait(5)

    # Redirect to URL
    #driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    yield driver  # This will pass the driver to the test function
    driver.quit()  # Cleanup: quit the driver after the test


# Function to fetch test data from the specified CSV file
def get_csv_data(file_path):
    with open(file_path, mode="r") as file:
        reader = csv.DictReader(file)
        return [row for row in reader]  # Returns a list of dictionaries


# Test using data from CSV
def test_example(test_verifyURL):
    # Specify the path to your CSV file
    csv_file_path = r"C:\Users\shoeb.syed\Downloads\csvread.csv"

    # Fetch test data from the CSV file
    test_data_list = get_csv_data(csv_file_path)

    for test_data in test_data_list:
        url = test_data["url"]
        username = test_data["username"]
        password = test_data["password"]

        # Open the URL
        driver.get(url)
        time.sleep(2)

        # Test steps
        driver.find_element("name", "username").send_keys(username)
        driver.find_element("name", "password").send_keys(password)


        # Navigate back to reset for the next test case
        driver.back()
        time.sleep(2)

