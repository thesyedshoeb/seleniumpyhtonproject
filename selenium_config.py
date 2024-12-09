from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def initialize_driver():
    """
    Initializes the Selenium WebDriver with the necessary configurations.

    Returns:
        WebDriver: An instance of the configured Chrome WebDriver.
    """
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    # Update the path as per your setup or use ChromeDriverManager for dynamic installation
    service = Service('C:\\Users\\shoeb.syed\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=service)
    driver.implicitly_wait(10)
    driver.maximize_window()
    return driver
