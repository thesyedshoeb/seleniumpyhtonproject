import json
import time
import allure
import pytest
import yaml
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def create_driver():
    global driver
    options=webdriver.ChromeOptions()
    options.add_experimental_option("detach",True)
    s=Service('C:\\Users\\shoeb.syed\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
    driver=webdriver.Chrome(options=options,service=s)
    driver.implicitly_wait(5)
    driver.get("https://www.amazon.in")
    driver.maximize_window()
    yield driver
    #driver.quit()

# 1. Login
'''
@allure.feature('Amazon Purchase Process')
@allure.story('Login to Amazon')
@pytest.mark.parametrize('email, password', [
    ('syed@123', 'qwerty@123')
])
def test_login(create_driver, email, password):
    time.sleep(10)
    sign_in_link = driver.find_element(By.ID, "nav-link-accountList")
    sign_in_link.click()

    mobile_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@type='email']"))
    )

    mobile_field.send_keys("9860680728")

    continue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@type='submit']"))
    )

    continue_button.click()

    password_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@type='password']"))
    )

    password_field.send_keys("ishoeb@123")

    sign_in_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@id='signInSubmit']"))
    )
    sign_in_button.click()

    time.sleep(15)
    otp_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@id='auth-signin-button']"))
    )
    otp_button.click()
'''

# 2. Search for Product
@allure.story('Search Product')
def test_search_product(create_driver):
    search_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@aria-label='Search Amazon.in']"))
    )
    search_field.send_keys("S24 ultra")

    search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@value='Go']"))
    )
    search_button.click()

    click_item = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Samsung Galaxy S24 Ultra 5G AI Smartphone (Titanium Gray, 12GB, 256GB Storage)']"))
    )
    driver.execute_script("arguments[0].scrollIntoView();", click_item)
    click_item.click()

# 3. Add Product to Cart
@allure.story('Add Product to Cart')
def test_add_to_cart():
    windows = driver.window_handles
    if len(windows) > 1:
        driver.switch_to.window(windows[1])
        print("Successfully switched to the second tab.")
    else:
        driver.switch_to.window(windows[0])
        print("Failed to switch to the second tab.")

    try:
        addtocart_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(// input[@ id='add-to-cart-button'])[2]"))
        )
        driver.execute_script("arguments[0].scrollIntoView();", addtocart_button)
        addtocart_button.click()
    except Exception as e:
        print(f"An error occurred: {e}")

# 4. Proceed to Checkout (Buy Now)
@allure.story('Proceed to Checkout')
def test_proceed_to_checkout():
    time.sleep(5)
    proceed_tocheckout = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@aria-labelledby= 'attach-sidesheet-checkout-button-announce']"))
    )
    proceed_tocheckout.click()

    mobile_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@type='email']"))
    )
    mobile_field.send_keys("9860680728")

    continue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@type='submit']"))
    )
    continue_button.click()

    password_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@type='password']"))
    )
    password_field.send_keys("ishoeb@123")

    sign_in_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@id='signInSubmit']"))
    )
    sign_in_button.click()

    time.sleep(15)
    '''otp_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@id='auth-signin-button']"))
    )
    otp_button.click()'''

# 5. Add Card Information
@allure.story('Add Card Information')
def test_add_card_information():
    useaddress_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@data-testid='Address_selectShipToThisAddress']"))
    )
    useaddress_button.click()

    card_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@id='pp-RS6OUT-161']"))
    )
    card_button.click()

    image_element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,
                                    "//img[@src='https://m.media-amazon.com/images/G/01/payments-portal/r1/PlusIcon._CB485933946_.gif']"))
    )
    image_element.click()


# 6. Confirm Payment
@allure.story('Confirm card details')
def test_confirm_payment():
    driver.switch_to.frame("ApxSecureIframe")
    driver.find_element(By.XPATH, "//input[@type='tel']").send_keys("4111 1111 4555 1142")
    time.sleep(3)
    month = driver.find_element(By.XPATH, "(//select[@data-a-native-class='pmts-native-dropdown'])[1]")
    sel = Select(month)
    sel.select_by_visible_text("03")
    # driver.find_element(By.XPATH,"//h4[@id='a-popover-header-1']").click()
    year = driver.find_element(By.XPATH, "(//select[@data-a-native-class='pmts-native-dropdown'])[2]")
    sel1 = Select(year)
    sel1.select_by_visible_text("2030")
    driver.find_element(By.XPATH, "//input[@name='ppw-widgetEvent:AddCreditCardEvent']").click()


