from selenium.webdriver.common.by import By
from pomproject.pages.base_page import BasePage

class LoginPage(BasePage):
    LOGIN_LINK = (By.LINK_TEXT, "Log in")
    EMAIL = (By.NAME, "Email")
    PASSWORD = (By.NAME, "Password")
    LOGIN_BUTTON = (By.XPATH, "//input[@value='Log in']")

    def login(self, email, password):
        self.click(self.LOGIN_LINK)
        self.send_keys(self.EMAIL, email)
        self.send_keys(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)
