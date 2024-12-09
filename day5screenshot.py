import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
s=Service('C:\\Users\\shoeb.syed\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
driver=webdriver.Chrome(options=options,service=s)

#context Click and move to element
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
time.sleep(5)

driver.save_screenshot("C:\\Users\\shoeb.syed\\Downloads\\planami2.png")