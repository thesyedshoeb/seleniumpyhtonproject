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
driver.implicitly_wait(10)

driver.get("https://www.amazon.in/")
driver.maximize_window()

driver.find_element("xpath","//input[@id='twotabsearchtextbox']").send_keys("iphone")
driver.find_element("xpath","//input[@id='nav-search-submit-button']").click()

'''driver.execute_script("window.scrollBy(0, 1000);")
driver.find_element("xpath","//span[text()='Apple iPhone 13 (128GB) - Starlight']").click()
#driver.execute_script("window.scrollBy(0, -1000);")'''


ele = driver.find_element("xpath","//span[text()='Apple iPhone 13 (128GB) - Starlight']")
# driver.execute_script("window.scrollBy(0, ele)")
driver.execute_script("arguments[0].scrollIntoView();", ele)
ele.click()



