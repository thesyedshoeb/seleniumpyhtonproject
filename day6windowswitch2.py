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
driver.get("https://toolsqa.com")
driver.maximize_window()

driver.find_element("xpath", "(//a[@href='https://demoqa.com'])[1]").click()
windows = driver.window_handles
if len(windows) >1 :
    driver.switch_to.window(windows[1])
element = driver.find_element("xpath", "//h5[text()='Elements']")
driver.execute_script("arguments[0].scrollIntoView();", element)
element.click()
print(driver.current_url)
#driver.switch_to.window(windows[0])
#ele = driver.find_element("css selector", ".new-training__heading")
#print(ele.text)