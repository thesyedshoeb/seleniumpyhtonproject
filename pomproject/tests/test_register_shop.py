import time
from pomproject.utils.driver_setup import get_driver
from pomproject.pages.registration_page import RegistrationPage
from pomproject.pages.login_page import LoginPage
from pomproject.pages.shopping_cart_page import ShoppingCartPage

class TestRegisterShop:
    def test_register_shop(self):
        driver = get_driver()

        try:
            # Registration
            reg_page = RegistrationPage(driver)
            reg_page.navigate_to_registration_page("https://demowebshop.tricentis.com/register")
            reg_page.fill_registration_form(
                first_name="Syed",
                last_name="Shoeb",
                email="shoeb.syed@infoneans.com",
                password="ishoeb@123",
                confirm_password="ishoeb@123"
            )

            # Login
            login_page = LoginPage(driver)
            login_page.login(email="shoeb.syed@infoneans.com", password="ishoeb@123")

            # Add item to cart
            cart_page = ShoppingCartPage(driver)
            cart_page.add_notebook_to_cart()
            cart_page.verify_cart_contains_item()

        finally:
            time.sleep(5)
            print("program getting closed")
            driver.quit()
