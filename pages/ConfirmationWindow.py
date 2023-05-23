from pages.BasePage import BasePage
from locators import MainPageLocators, ConfirmationWindowLocators


class ConfirmationWindow(BasePage):
    def check_confirmation_window(self):
        return self.find_element(ConfirmationWindowLocators.CONFIRMATION_ADDING_TO_BASKET)

    def close_confirmation_window(self):
        return self.find_element(ConfirmationWindowLocators.CLOSE_CONFIRMATION_WINDOW).click()

    def to_increase_count(self):
        self.find_element(ConfirmationWindowLocators.TO_INCREASE_COUNT).click()

    def check_quantity_of_products(self):
        counter = self.find_element(ConfirmationWindowLocators.COUNTER)
        value = counter.get_attribute("value")
        return value

    def go_to_basket(self):
        self.find_element(ConfirmationWindowLocators.TO_BASKET).click()