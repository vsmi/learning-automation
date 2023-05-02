from pages.BaseApp import BasePage
from locators import MainPageLocators, ConfirmationWindowLocators, BasketLocators


class Basket(BasePage):
    def check_basket(self):
        return self.find_element(BasketLocators.BASKET)

