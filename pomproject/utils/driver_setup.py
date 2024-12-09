from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(options=options, service=service)
    driver.implicitly_wait(5)
    return driver
