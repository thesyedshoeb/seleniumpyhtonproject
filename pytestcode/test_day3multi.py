import json
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

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
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    yield driver  # This will pass the driver to the test function
    driver.quit()  # Cleanup: quit the driver after the test

# Fixture to load test cases from JSON
#@pytest.fixture(scope="session")
def load_test_data():
    with open("multi.json", "r") as file:
        return json.load(file)["test_case"]


# Parameterize tests with data from the JSON file
@pytest.mark.parametrize("test_case", load_test_data())
def test_example(test_verifyURL, test_case):
    # Extract data for the current test case
    url = test_case["url"]
    username = test_case["username"]
    password = test_case["password"]

    # Open the URL
    driver.get(url)
    time.sleep(4)

    # Perform test steps
    driver.find_element("name", "username").send_keys(username)
    driver.find_element("name", "password").send_keys(password)
    driver.find_element("xpath", "//button[@type='submit']").click()
