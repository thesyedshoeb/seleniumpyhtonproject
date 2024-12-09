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


@pytest.fixture()
def test_verifyURL():

    global driver
    options=webdriver.ChromeOptions()
    options.add_experimental_option("detach",True)
    s=Service('C:\\Users\\shoeb.syed\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
    driver=webdriver.Chrome(options=options,service=s)
    driver.implicitly_wait(5)

    #Redirect to URL.
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    print("enter in test_verifyURL()")

# Fixture to load data from the YAML file
@pytest.fixture()
def config_data_yaml():
    with open("config.yaml", "r") as file:
        return yaml.safe_load(file)  # Returns the content as a dictionary

@pytest.fixture()
def config_data_json():
    with open("config.json", "r") as file:
        return json.load(file)  # Returns the content as a dictionary

def test_exampleyaml(test_verifyURL, config_data_yaml):
    # Use data from the YAML configuration
    url = config_data_yaml["url"]
    username = config_data_yaml["username"]
    password = config_data_yaml["password"]

    # Open the URL
    driver.get(url)
    time.sleep(4)

    # Test steps
    driver.find_element("name", "username").send_keys(username)
    driver.find_element("name", "password").send_keys(password)
    driver.find_element("xpath", "//button[@type='submit']").click()

def test_examplejson(test_verifyURL,config_data_json):
    # Use data from the YAML configuration
    url = config_data_json["url"]
    username = config_data_json["username"]
    password = config_data_json["password"]

    # Open the URL
    driver.get(url)
    time.sleep(4)

    # Test steps
    driver.find_element("name", "username").send_keys(username)
    driver.find_element("name", "password").send_keys(password)
    driver.find_element("xpath", "//button[@type='submit']").click()

