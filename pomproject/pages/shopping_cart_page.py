from selenium.webdriver.common.by import By
from pomproject.pages.base_page import BasePage

class ShoppingCartPage(BasePage):
    COMPUTERS_MENU = (By.LINK_TEXT, "Computers")
    NOTEBOOKS_LINK = (By.LINK_TEXT, "Notebooks")
    ADD_TO_CART_BUTTON = (By.XPATH, "//input[@value='Add to cart']")
    SHOPPING_CART = (By.XPATH, "//span[text()='Shopping cart']")

    def add_notebook_to_cart(self):
        self.click(self.COMPUTERS_MENU)
        self.click(self.NOTEBOOKS_LINK)
        self.click(self.ADD_TO_CART_BUTTON)

    def verify_cart_contains_item(self):
        cart = self.find_element(self.SHOPPING_CART)
        print(cart.text)
        cart.click()
