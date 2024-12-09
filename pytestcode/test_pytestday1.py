import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from trio._subprocess_platform import windows
from webdriver_manager.chrome import ChromeDriverManager
import pytest

#command to run smoke regression
#pytest -m "smoke or regression" test_New1.py
#command to print in console
# pytest -m "regression" test_pytestday1.py -s


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

@pytest.mark.smoke
def test_clickBooks(test_verifyURL):
    driver.find_element("xpath", "(//a[contains(text(),'Books')])[1]").click()
    print("enter in test_clickBooks()")

@pytest.mark.regression
@pytest.mark.click
def test_clickComputers(test_verifyURL):
    driver.find_element("xpath", "(//a[contains(text(),'Computers')])[1]").click()
    print("enter in test_clickBooks()")

#@pytest.mark.skip("skipping")
@pytest.mark.smoke
def test_clicklogout():
    print("enter in test_clicklogout")