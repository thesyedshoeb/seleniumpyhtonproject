import time
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
from selenium.webdriver.support.ui import Select


@pytest.fixture()
def test_verifyURL():

    global driver
    options=webdriver.ChromeOptions()
    options.add_experimental_option("detach",True)
    s=Service('C:\\Users\\shoeb.syed\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
    driver=webdriver.Chrome(options=options,service=s)
    driver.implicitly_wait(5)

    #Redirect to URL.
    driver.get("https://blazedemo.com/")
    driver.maximize_window()
    time.sleep(2)
    print("enter in test_verifyURL()")

@allure.title("Find Flight")
@allure.feature("Find Flight")
@allure.story("SWC-121")
@pytest.mark.smoke
def test_findFlight(test_verifyURL):
    departurecity = driver.find_element("xpath", "//select[@name='fromPort']")
    sel=Select(departurecity)
    sel.select_by_visible_text("Philadelphia")
    destinationcity=driver.find_element("xpath","//select[@name='toPort']")
    sel1=Select(destinationcity)
    sel1.select_by_visible_text("Rome")
    driver.find_element("xpath","//input[@class='btn btn-primary']").click()
    time.sleep(3)
    driver.find_element("xpath","(//input[@class='btn btn-small'])[2]").click()
    time.sleep(3)

@allure.title("Choose Flight")
@allure.feature("Choose Flight")
@allure.story("SWC-122")
@pytest.mark.smoke
def test_chooseFlight():
    Flight = driver.find_element("xpath", "(//div[@class='container'])[2]")
    print(Flight.text)

@allure.title("Flight Details")
@allure.feature("Flight Details")
@allure.story("SWC-123")
@pytest.mark.regression
def test_enterDetailsFlight():
    driver.find_element("xpath", "//input[@id='inputName']").send_keys("Somesh")
    driver.find_element("xpath", "//input[@id='address']").send_keys("Address")
    driver.find_element("xpath", "//input[@id='city']").send_keys("city")
    driver.find_element("xpath", "//input[@id='state']").send_keys("California")
    driver.find_element("xpath", "//input[@id='zipCode']").send_keys("345262")
    driver.find_element("xpath", "//input[@id='creditCardNumber']").send_keys("37473747345345345")
    driver.find_element("xpath", "//input[@id='creditCardMonth']").send_keys("03")
    driver.find_element("xpath", "//input[@id='creditCardYear']").send_keys("2024")
    driver.find_element("xpath", "//input[@id='nameOnCard']").send_keys("USA")
    cardtype = driver.find_element("xpath", "//select[@class='form-inline']")
    sel2 = Select(cardtype)
    sel2.select_by_visible_text("American Express")
    time.sleep(2)
    driver.find_element("xpath", "//input[@type='checkbox']").click()

@allure.title("Flight Purchase")
@allure.feature("Flight Purchase")
@allure.story("SWC-124")
@pytest.mark.regression
def test_purchaseflight():
    driver.find_element("xpath", "//input[@class='btn btn-primary']").click()
    time.sleep(3)
    purchase = driver.find_element("xpath", "//div[@class='container hero-unit']")
    print(purchase.text)

