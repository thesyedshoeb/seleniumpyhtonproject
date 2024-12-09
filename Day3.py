import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
s=Service('C:\\Users\\shoeb.syed\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
driver=webdriver.Chrome(options=options,service=s)
driver.get("https://demowebshop.tricentis.com/register")
driver.maximize_window()
time.sleep(4)
print(driver.title)
print(driver.current_url)
time.sleep(4)

driver.find_element("id", "gender-male").click()
driver.find_element("name","FirstName").send_keys("Syed")
driver.find_element("name","LastName").send_keys("Shoeb")
driver.find_element("name","Email").send_keys("shoeb.syed@infoneans.com")
driver.find_element("name","Password").send_keys("ishoeb@123")
driver.find_element("name", "ConfirmPassword").send_keys("ishoeb@123")
driver.find_element("id","register-button").click()
driver.find_element("link text","Log in").click()
driver.find_element("name","Email").send_keys("shoeb.syed@infoneans.com")
driver.find_element("name","Password").send_keys("ishoeb@123")
driver.find_element("xpath","//input[@value='Log in']").click()
driver.find_element("link text" , "Desktops").click()




