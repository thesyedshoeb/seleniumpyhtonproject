import time
import pytest
from pomproject.utils.driver_setup import get_driver
from pomproject.pages.registration_page import RegistrationPage
from pomproject.pages.login_page import LoginPage
from pomproject.pages.shopping_cart_page import ShoppingCartPage
from pomproject.pages.base_page import BasePage

@pytest.fixture(scope="class")
def setup_driver(request):
    """Fixture to set up and tear down the driver."""
    driver = get_driver()
    request.cls.driver = driver
    yield
    time.sleep(2)
    print("Closing the browser and quitting the driver.")
    driver.quit()

@pytest.mark.usefixtures("setup_driver")
class TestRegisterShop:

    def test_registration(self):
        """Test user registration functionality."""
        reg_page = RegistrationPage(self.driver)
        reg_page.navigate_to_registration_page("https://demowebshop.tricentis.com/register")
        reg_page.fill_registration_form(
            first_name="Syed",
            last_name="Shoeb",
            email="shoeb.syed@infoneans.com",
            password="ishoeb@123",
            confirm_password="ishoeb@123"
        )
        print("Registration test completed.")

    def test_login(self):
        """Test user login functionality."""
        login_page = LoginPage(self.driver)
        reg_page = RegistrationPage(self.driver)
        reg_page.navigate_to_registration_page("https://demowebshop.tricentis.com")
        login_page.login(email="shoeb.syed@infoneans.com", password="ishoeb@123")
        print("Login test completed.")

    def test_add_to_cart(self):
        """Test adding a notebook to the shopping cart."""
        cart_page = ShoppingCartPage(self.driver)
        cart_page.add_notebook_to_cart()
        print("Add to cart test completed.")

    def test_verify_cart(self):
        """Test verifying the shopping cart contains the item."""
        cart_page = ShoppingCartPage(self.driver)
        cart_page.verify_cart_contains_item()
        print("Verify cart test completed.")
