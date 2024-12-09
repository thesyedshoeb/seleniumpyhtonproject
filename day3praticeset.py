import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
s=Service('C:\\Users\\shoeb.syed\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
driver=webdriver.Chrome(options=options,service=s)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()
element=driver.find_element("xpath","//a[contains(text(),'Register')]")
print(element.text)
print(element.tag_name)
element.click()
Email="shoeb.syed@infoneans.com"
Password="ishoeb@123"
#driver.find_element("xpath","//a[contains(text(),'Register')]").click()
#driver.find_element("link text","Register").click()
#driver.find_element("partial link text","Register").click()

driver.find_element("xpath","//input[@id='gender-male']").click()
driver.find_element("xpath","//input[@id='FirstName']").send_keys("Syed")
driver.find_element("xpath","//input[@id='LastName']").send_keys("Shoeb")
driver.find_element("xpath","//input[@id='Email']").send_keys(Email)
driver.find_element("xpath","//input[@id='Password']").send_keys(Password)
driver.find_element("xpath","//input[@id='ConfirmPassword']").send_keys(Password)
driver.find_element("xpath","//input[@id='register-button']").click()
time.sleep(4)
driver.find_element("link text","Log in").click()
driver.find_element("xpath","//input[@id='Email']").send_keys(Email)
driver.find_element("xpath","//input[@id='Password']").send_keys(Password)
driver.find_element("xpath","//input[@class='button-1 login-button']").click()
driver.find_element("xpath","(//a[contains(text(),'Computers')])[1]").click()
driver.find_element("xpath","(//a[contains(text(),'Desktops')])[4]").click()
time.sleep(5)
driver.find_element("xpath","(//input[@type='button'])[3]").click()
time.sleep(5)
driver.find_element("xpath","(//input[@type='button'])[3]").click()
time.sleep(1)
#abc=driver.find_element("xpath","//p[contains(text(),'The product has been added to your')]")
#print(abc.text)
driver.find_element("link text","shopping cart").click()