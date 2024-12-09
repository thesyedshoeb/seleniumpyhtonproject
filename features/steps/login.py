import logger
from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


@given(u'open browser')
def step_impl(context):
    global driver
    options = webdriver.ChromeOptions()
    #options.add_argument("--headless")  # Run headless
    options.add_experimental_option("detach", True)  # Keep the browser open after test finishes
    service = Service('C:\\Users\\shoeb.syed\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=service)
    driver.implicitly_wait(5)

    # Redirect to URL
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()


@when(u'enter username "Admin" password "admin123"')
def step_impl(context):
    driver.find_element("name", "username").send_keys("Admin")
    driver.find_element("name", "password").send_keys("admin123")


@then(u'click login button')
def step_impl(context):
    driver.find_element("xpath", "//button[@type='submit']").click()


@given(u'click search button')
def step_impl(context):
    # logger.info(driver.title)
    print(driver.title)
    driver.find_element("xpath", "//input[@placeholder='Search']").send_keys("shoeb")




