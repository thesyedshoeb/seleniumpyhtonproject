import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
s=Service('C:\\Users\\shoeb.syed\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
driver=webdriver.Chrome(options=options,service=s)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(4)
print(driver.title)
print(driver.current_url)
time.sleep(4)

driver.find_element("name","username").send_keys("Admin")
driver.find_element("name","password").send_keys("admin123")
driver.find_element("xpath","//button[@type='submit']").click()

'''
#check git pull
driver.find_element("xpath","//input[@name='username']").send_keys("Admin")
driver.find_element("xpath","//input[@name='password']").send_keys("admin123")
driver.find_element("xpath","//button[@type='submit']").click()

Xpath by attribute

//tagname[@attribute='Value']

Xpath by Text:
//tagname[text()='Value']


Xpath by Contains:when xpath is dynamic

//tagname[contains(text(),'value')]

//a[contains(text(),'Books')]


(//a[contains(text(),'Books')])[1]

'''
