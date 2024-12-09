import logging
from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import allure

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# Global driver variable
driver = None

# Step for opening the browser
@given(u'I open the chrome browser')
def step_impl(context):
    global driver
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")  # Run headless (no UI)
    options.add_experimental_option("detach", True)  # Keep browser open after test
    service = Service('C:\\Users\\shoeb.syed\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=service)
    driver.implicitly_wait(5)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()


@when(u'I enter username {username} and password {password}')
def step_impl(context, username, password):
    driver.find_element("name", "username").send_keys(username)
    driver.find_element("name", "password").send_keys(password)

# Step for clicking the login button
@then(u'I click the login buttons')
def step_impl(context):
    driver.find_element("xpath", "//button[@type='submit']").click()

