import time

from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from trio._subprocess_platform import windows
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import allure

#command to run smoke regression
#pytest -m "smoke or regression" test_New1.py
#command to print in console
# pytest -m "regression" test_pytestday1.py -s
#command to run particular function
#pytest test_example.py::test_function1
#commandto run two function
#pytest test_example.py::test_function1 test_example.py::test_function2

@pytest.fixture()
def test_verifyURL():

    global driver
    options=webdriver.ChromeOptions()
    options.add_experimental_option("detach",True)
    s=Service('C:\\Users\\shoeb.syed\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
    driver=webdriver.Chrome(options=options,service=s)
    driver.implicitly_wait(5)

    #Redirect to URL.
    driver.get("https://demowebshop.tricentis.com/")
    driver.maximize_window()
    print("enter in test_verifyURL()")

@allure.title("assert failed")
@pytest.mark.assertBooks
def test_clickBook(test_verifyURL):
    expected_title = "Demo Web Shop"
    actual_title = driver.title
    # Assert that the actual title matches the expected title
    assert actual_title == expected_title, f"Title mismatch: Expected '{expected_title}"
    driver.find_element("xpath","(//a[contains(text(),'Books')])[1]").click()
    assert "books" in driver.current_url.lower(), "Failed to navigate to Books page"
    allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

@pytest.mark.smoke
def test_clickBooks():
    driver.find_element("xpath", "(//a[contains(text(),'Books')])[1]").click()
    print("enter in test_clickBooks()")

@pytest.mark.regression
@pytest.mark.click
def test_clickComputers():
    driver.find_element("xpath", "(//a[contains(text(),'Computers')])[1]").click()
    print("enter in test_clickBooks()")

#@pytest.mark.skip("skipping")
@pytest.mark.smoke
def test_clicklogout():
    print("enter in test_clicklogout")