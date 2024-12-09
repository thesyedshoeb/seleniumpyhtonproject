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

driver.get("https://the-internet.herokuapp.com/frames")
driver.maximize_window()
time.sleep(5)

driver.find_element("link text" , "Nested Frames").click()
driver.switch_to.frame("frame-top")
print("shifted to frame top")

driver.switch_to.frame("frame-left")
print("shifted to frame left")
left=driver.find_element("xpath","//body[contains(text(),'LEFT')]").text
print(left)

driver.switch_to.parent_frame()
print("shifted to frame top")

driver.switch_to.frame("frame-middle")
print("shifted to frame middle")
MIDDLE=driver.find_element("xpath","//div[text()='MIDDLE']")

driver.switch_to.parent_frame()
print("shifted to frame top")

driver.switch_to.frame("frame-right")
print("shifted to frame right")
right=driver.find_element("xpath","//body[contains(text(),'RIGHT')]").text

driver.switch_to.parent_frame()
print("shifted to frame top")

driver.switch_to.default_content()

driver.switch_to.frame("frame-bottom")
print("shifted to frame bottom")
bottom=driver.find_element("xpath","//body[contains(text(),'BOTTOM')]").text

driver.switch_to.default_content()


#driver.switch_to.frame(driver.find_element("xpath","//iframe[@id='frm']"))
#abc=driver.find_element("xpath","//body[contains(text(),'LEFT')]").text
#print(abc)

'''driver.find_element("id","fn").send_keys("Plabani")
driver.switch_to.frame("frm")
driver.find_element("id","mn").send_keys("M")
driver.switch_to.default_content()
#driver.switch_to.parent_frame()
driver.find_element("id","ln").send_keys("n")'''