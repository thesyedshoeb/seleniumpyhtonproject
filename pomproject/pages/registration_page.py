from selenium.webdriver.common.by import By
from pomproject.pages.base_page import BasePage

class RegistrationPage(BasePage):
    GENDER_MALE = (By.ID, "gender-male")
    FIRST_NAME = (By.ID, "FirstName")
    LAST_NAME = (By.ID, "LastName")
    EMAIL = (By.ID, "Email")
    PASSWORD = (By.ID, "Password")
    CONFIRM_PASSWORD = (By.ID, "ConfirmPassword")
    REGISTER_BUTTON = (By.ID, "register-button")

    def navigate_to_registration_page(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def fill_registration_form(self, first_name, last_name, email, password, confirm_password):
        self.click(self.GENDER_MALE)
        self.send_keys(self.FIRST_NAME, first_name)
        self.send_keys(self.LAST_NAME, last_name)
        self.send_keys(self.EMAIL, email)
        self.send_keys(self.PASSWORD, password)
        self.send_keys(self.CONFIRM_PASSWORD, confirm_password)
        self.click(self.REGISTER_BUTTON)
