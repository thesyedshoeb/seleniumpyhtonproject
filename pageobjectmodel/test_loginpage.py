import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pageobjectmodel.login_page import loginPage


@pytest.fixture(scope="module")
def setup():
    global driver
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)  # Keep the browser open after test finishes
    service = Service('C:\\Users\\shoeb.syed\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=service)
    driver.implicitly_wait(5)

    # Redirect to URL
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    yield driver  # This will pass the driver to the test function
    #driver.quit()  # Cleanup: quit the driver after the test


def test_valid_login(setup):
    driver = setup
    login_page = loginPage(driver)

    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
    login_page.click_login_button()
    # Perform valid login
    #login_page.login("Admin", "admin123")
