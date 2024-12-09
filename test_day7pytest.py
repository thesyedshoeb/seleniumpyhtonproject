from selenium_config import initialize_driver
import pytest
# Initialize the driver
driver = initialize_driver()
driver.get("https://toolsqa.com")
driver.maximize_window()
