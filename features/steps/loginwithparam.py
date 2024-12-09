import logging
from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import allure
#to install reports
#pip install behave-html-formatter
#to run the reports
#behave --format behave_html_formatter:HTMLFormatter --outfile=reports/report.html
#to view the reports
#start reports/report.html


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# Global driver variable
driver = None

# Step for opening the browser
@given(u'I open the browser')
@allure.step("Opening the browser")
def step_impl(context):
    global driver
    options = webdriver.ChromeOptions()
    #options.add_argument("--headless")  # Run headless (no UI)
    options.add_experimental_option("detach", True)  # Keep browser open after test
    service = Service('C:\\Users\\shoeb.syed\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=service)
    driver.implicitly_wait(5)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    allure.attach(driver.get_screenshot_as_png(), name="Browser opened", attachment_type=allure.attachment_type.PNG)

# Step for entering the username and password
@when(u'I enter username "{username}" and password "{password}"')
@allure.step("Entering username and password")
def step_impl(context, username, password):
    driver.find_element("name", "username").send_keys(username)
    driver.find_element("name", "password").send_keys(password)
    allure.attach(driver.get_screenshot_as_png(), name="Username and Password entered", attachment_type=allure.attachment_type.PNG)

# Step for clicking the login button
@then(u'I click the login button')
@allure.step("Clicking the login button")
def step_impl(context):
    driver.find_element("xpath", "//button[@type='submit']").click()
    allure.attach(driver.get_screenshot_as_png(), name="Login button clicked", attachment_type=allure.attachment_type.PNG)

# Step for clicking the search button (for search scenario)
@given(u'I click the search button')
@allure.step("Clicking the search button")
def step_impl(context):
    # This can be modified to perform a search as per your needs
    print(driver.title)  # You can log or assert page title for verification
    driver.find_element("xpath", "//input[@placeholder='Search']").send_keys("shoeb")
    allure.attach(driver.get_screenshot_as_png(), name="Search button clicked", attachment_type=allure.attachment_type.PNG)
