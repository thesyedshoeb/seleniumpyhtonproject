import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
s=Service('C:\\Users\\shoeb.syed\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
driver=webdriver.Chrome(options=options,service=s)
driver.get("https://demowebshop.tricentis.com/books?orderby=10")
driver.maximize_window()
time.sleep(4)
x=driver.find_element("xpath","//select [@id='products-orderby']")
sel=Select(x)
time.sleep(4)

sel.select_by_index(4)

#sel.select_by_value("https://demowebshop.tricentis.com/books?orderby=6")

#sel.select_by_visible_text("Created on")