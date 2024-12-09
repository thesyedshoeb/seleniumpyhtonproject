#Window handling program of toolqa site.


import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from trio._subprocess_platform import windows
from webdriver_manager.chrome import ChromeDriverManager


# services
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
s=Service('C:\\Users\\shoeb.syed\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe')
driver=webdriver.Chrome(options=options,service=s)
driver.implicitly_wait(5)

#Redirect to URL.
driver.get("https://toolsqa.com/")
driver.maximize_window()
wait = WebDriverWait(driver, 10)

#To accept cookies
try:
    cookie_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@id='accept-cookie-policy']")))
    cookie_button.click()
except:
    print("Cookie button Element not found")

#To click on "Demo Site".
try:
    Demo_site = wait.until(EC.element_to_be_clickable((By.XPATH, "//ul[@class='navbar__links d-none d-lg-flex']//a[normalize-space()='Demo Site']")))
    Demo_site.click()
except:
    print("Demo site Element not found")

#To handle first opened window
all_window_handles = driver.window_handles
main_window_handle = driver.current_window_handle
if len(all_window_handles) > 1 :
    new_tab_handle = [handle for handle in all_window_handles if handle != main_window_handle][0]
    driver.switch_to.window(new_tab_handle)
    time.sleep(1)
    print(f"Switched to new tab: {driver.title}")

#To click on Join now.
try:
    Join_now = wait.until(EC.element_to_be_clickable((By.XPATH, "//img[@src='/images/WB.svg']")))
    Join_now.click()

except:
    print("Element not found")

#To handle second opened window
all_window_handles = driver.window_handles
main_window_handle = driver.current_window_handle
if len(all_window_handles) > 1 :
    new_tab_handle = [handle for handle in all_window_handles if handle != main_window_handle][1]
    driver.switch_to.window(new_tab_handle)
    time.sleep(1)
    print(f"Switched to new tab: {driver.title}")

#To land on registration page.
try:
    Registration_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@class='btn btn-primary-shadow btn-block']")))
    Registration_button.click()
except:
    print("Element not found")
finally:
    print("Successfully landed on Registration page")