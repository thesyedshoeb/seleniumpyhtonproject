import time

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys


@pytest.fixture()

def test_verifyURL():

    global driver
    options=webdriver.ChromeOptions()
    options.add_experimental_option("detach",True)
    s=Service('C:\\Users\\shoeb.syed\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
    driver=webdriver.Chrome(options=options,service=s)
    driver.implicitly_wait(5)

    #Redirect to URL.
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    print("enter in test_verifyURL()")


# Parameterize test with different usernames and passwords
@pytest.mark.parametrize(
    "username, password",
    [
        ("Admin", "admin123"),       # Valid credentials
        ("invalid_user", "admin123"), # Invalid username
        ("Admin", "wrongpassword"),  # Invalid password
        ("", ""),                    # Empty credentials
    ]
)

@allure.title("login with different username")
@allure.feature("login")
@allure.story("SWC-121")
@pytest.mark.smoke
def test_login(test_verifyURL, username, password):
    # Locate and interact with username field

    username_field = driver.find_element("name", "username")
    username_field.send_keys(username)

    # Locate and interact with password field
    password_field = driver.find_element("name", "password")
    # password_field.clear()
    password_field.send_keys(password)

    # Click login button
    login_button = driver.find_element("xpath", "//button[@type='submit']")
    login_button.click()
    allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)



