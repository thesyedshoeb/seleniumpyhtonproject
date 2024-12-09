import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
s=Service('C:\\Users\\shoeb.syed\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
driver=webdriver.Chrome(options=options,service=s)
driver.get("https://www.softwaretestingmaterial.com/sample-webpage-to-automate/")
driver.maximize_window()
time.sleep(4)
x=driver.find_element("xpath","(//select[@class='spTextField'])[1]")
sel=Select(x)
time.sleep(4)
sel.select_by_index(2)
time.sleep(2)

sel.select_by_index(3)
sel.deselect_all()