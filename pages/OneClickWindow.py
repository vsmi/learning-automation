from pages.BasePage import BasePage
from locators import MainPageLocators, OneClickLocators


class OneClickWindow(BasePage):
    def check_one_click_window(self):
        return self.find_element(OneClickLocators.ONECLICK)

    def enter_name(self, name):
        name_field = self.find_element(OneClickLocators.NAME)
        name_field.click()
        name_field.send_keys(name)
        return name_field

    def enter_email(self, email):
        email_field = self.find_element(OneClickLocators.EMAIL)
        email_field.click()
        email_field.send_keys(email)
        return email_field

    def enter_phone(self, phone):
        phone_field = self.find_element(OneClickLocators.PHONE)
        phone_field.click()
        phone_field.send_keys(phone)
        return phone_field

    def check_valid(self, elem):
        return self.get_attribute_of_elem(elem)

