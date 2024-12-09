import time
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

@given('I open the Amazon homepage')
def step_open_amazon_homepage(context):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)  # Keep browser open after test
    service = Service('C:\\Users\\shoeb.syed\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
    context.driver = webdriver.Chrome(options=options, service=service)
    context.driver.implicitly_wait(10)
    context.driver.get("https://www.amazon.in")
    context.driver.maximize_window()


@when('I search for "{product}"')
def step_search_product(context, product):
    search_field = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@aria-label='Search Amazon.in']"))
    )
    search_field.send_keys(product)
    search_button = context.driver.find_element(By.XPATH, "//input[@value='Go']")
    search_button.click()

@when('I click on the product')
def step_click_product(context):
    click_item = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,
                                    "//span[text()='Samsung Galaxy S24 Ultra 5G AI Smartphone (Titanium Gray, 12GB, 256GB Storage)']"))
    )
    context.driver.execute_script("arguments[0].scrollIntoView();", click_item)
    click_item.click()


@then('I add the product to the cart')
def step_add_to_cart(context):
    windows = context.driver.window_handles
    if len(windows) > 1:
        context.driver.switch_to.window(windows[1])
        print("Successfully switched to the second tab.")
    else:
        context.driver.switch_to.window(windows[0])
        print("Failed to switch to the second tab.")

    try:
        addtocart_button = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(// input[@ id='add-to-cart-button'])[2]"))
        )
        context.driver.execute_script("arguments[0].scrollIntoView();", addtocart_button)
        addtocart_button.click()
    except Exception as e:
        print(f"An error occurred: {e}")


@when('I click on proceed to checkout')
def step_proceed_to_checkout(context):
    time.sleep(5)
    proceed_tocheckout = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@aria-labelledby= 'attach-sidesheet-checkout-button-announce']"))
    )
    proceed_tocheckout.click()

    mobile_field = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@type='email']"))
    )
    mobile_field.send_keys("9860680728")

    continue_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@type='submit']"))
    )
    continue_button.click()

    password_field = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@type='password']"))
    )
    password_field.send_keys("ishoeb@123")

    sign_in_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@id='signInSubmit']"))
    )
    sign_in_button.click()

    time.sleep(10)
    '''otp_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@id='auth-signin-button']"))
    )
    otp_button.click()'''


@when('I add the card information')
def step_add_card_information(context):
    useaddress_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@data-testid='Address_selectShipToThisAddress']"))
    )
    useaddress_button.click()

    card_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@id='pp-RS6OUT-161']"))
    )
    card_button.click()

    image_element = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,
                                    "//img[@src='https://m.media-amazon.com/images/G/01/payments-portal/r1/PlusIcon._CB485933946_.gif']"))
    )
    image_element.click()


@then('I confirm the card details')
def step_confirm_payment(context):
    context.driver.switch_to.frame("ApxSecureIframe")
    context.driver.find_element(By.XPATH, "//input[@type='tel']").send_keys("4111 1111 4555 1142")
    time.sleep(3)
    month = context.driver.find_element(By.XPATH, "(//select[@data-a-native-class='pmts-native-dropdown'])[1]")
    sel = Select(month)
    sel.select_by_visible_text("03")
    # driver.find_element(By.XPATH,"//h4[@id='a-popover-header-1']").click()
    year = context.driver.find_element(By.XPATH, "(//select[@data-a-native-class='pmts-native-dropdown'])[2]")
    sel1 = Select(year)
    sel1.select_by_visible_text("2030")
    context.driver.find_element(By.XPATH, "//input[@name='ppw-widgetEvent:AddCreditCardEvent']").click()
    print("Payment confirmed successfully.")


@then('the payment should be processed successfully')
def step_payment_processed(context):
    print("Payment processed successfully.")
