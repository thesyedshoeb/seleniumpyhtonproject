import time
from argparse import Action

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
s=Service('C:\\Users\\shoeb.syed\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
driver=webdriver.Chrome(options=options,service=s)
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()
time.sleep(4)
elementsource=driver.find_element("xpath","//div[@id='box1']")
elementtarget=driver.find_element("xpath","//div[@id='box106']")
hover = ActionChains(driver)
hover.drag_and_drop(elementsource, elementtarget).perform()

