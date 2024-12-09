import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from behave import given, when, then

def initialize_driver():
    global driver
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")  # Run headless (no UI)
    options.add_experimental_option("detach", True)  # Keep browser open after test
    service = Service('C:\\Users\\shoeb.syed\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=service)
    driver.implicitly_wait(5)
    return driver

@given("I navigate to the Demo Webshop registration page")
def step_navigate_to_registration(context):
    context.driver = initialize_driver()
    context.driver.get("https://demowebshop.tricentis.com/register")
    context.driver.maximize_window()
    time.sleep(4)

@when("I fill out the registration form and register")
def step_fill_registration_form(context):
    context.driver.find_element(By.XPATH, "//*[@id='gender-male']").click()
    context.driver.find_element(By.XPATH, "//*[@id='FirstName']").send_keys("Syed")
    context.driver.find_element(By.XPATH, "//*[@id='LastName']").send_keys("Shoeb")
    context.driver.find_element(By.XPATH, "//*[@id='Email']").send_keys("shoeb.syed@infoneans.com")
    context.driver.find_element(By.XPATH, "//*[@id='Password']").send_keys("ishoeb@123")
    context.driver.find_element(By.XPATH, "//*[@id='ConfirmPassword']").send_keys("Nov2024")
    context.driver.find_element(By.XPATH, "//*[@id='register-button']").click()
    time.sleep(4)

@then("I should be able to log in with my registered credentials")
def step_login_with_credentials(context):
    context.driver.find_element(By.XPATH, "//a[text()='Log in']").click()
    context.driver.find_element(By.NAME, "Email").send_keys("shoeb.syed@infoneans.com")
    context.driver.find_element(By.NAME, "Password").send_keys("ishoeb@123")
    context.driver.find_element(By.XPATH, "//input[@value='Log in']").click()
    time.sleep(4)

@when("I add a notebook to the shopping cart")
def step_add_to_cart(context):
    context.driver.find_element(By.LINK_TEXT, "Computers").click()
    context.driver.find_element(By.LINK_TEXT, "Notebooks").click()
    context.driver.find_element(By.XPATH, "//input[@value='Add to cart']").click()
    time.sleep(4)

@then("I verify the shopping cart contains the item")
def step_verify_cart(context):
    cart = context.driver.find_element(By.XPATH, "//span[text()='Shopping cart']")
    print(cart.text)
    print(cart.tag_name)
    cart.click()
    time.sleep(4)
