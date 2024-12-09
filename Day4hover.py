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
element=driver.find_element("xpath","(//a[contains(text(),'Computers')])[1]")
a=ActionChains(driver)
a.move_to_element(element).perform()
a.context_click(element).perform()

#double click
'''driver.get("https://demo.guru99.com/test/simple_context_menu.html")
driver.maximize_window()
time.sleep(4)
#element=driver.find_element("xpath","//body[@id='authentication']/button")
element=driver.find_element("xpath","//button[text()='Double-Click Me To See Alert']")
a=ActionChains(driver)
a.double_click(element).perform()'''