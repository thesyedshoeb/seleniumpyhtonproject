from selenium_config import initialize_driver

# Initialize the driver
driver = initialize_driver()
driver.get("https://toolsqa.com")
driver.maximize_window()

driver.find_element("xpath","(//a[contains(text(),'Demo Site')])[1]").click()

# Get all window handles (including the main window and the new tab)
main_window_handle = driver.current_window_handle
all_window_handles = driver.window_handles

# Find the handle of the new tab (excluding the main window handle)
new_tab_handle = [handle for handle in all_window_handles if handle != main_window_handle][0]

# Switch to the new tab
driver.switch_to.window(new_tab_handle)
driver.find_element("xpath","//img[@alt='Selenium Online Training']").click()
print(driver.current_url)


'''if len(all_window_handles) > 1:
    # Find the handle of the new tab (exclude the main window handle)
    new_tab_handle = [handle for handle in all_window_handles if handle != main_window_handle][0]

    # Switch to the new tab
    driver.switch_to.window(new_tab_handle)'''