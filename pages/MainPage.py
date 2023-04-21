from pages.BaseApp import BasePage
from locators import Locators


class MainPage(BasePage):
    """
    ищет элемент строки поиска, кликает и вводит в поиск необходимое слово
    """
    def enter_word(self, word):
        search_field = self.find_element(Locators.SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    """
    ищет элемент кнопки поиска и кликает на неё
    """
    def click_on_the_search_button(self):
        return self.find_element(Locators.SEARCH_BTN, time=2).click()

    def check_search_result(self):
        all_list = self.find_elements(Locators.PRODUCTS_LIST, time=2)
        search_result = [x.text for x in all_list if len(x.text) > 0]
        return search_result

    def click_on_the_login_button(self):
        return self.find_element(Locators.LOGIN_BTN, time=2).click()

    def check_auth_form(self):
        return self.find_element(Locators.AUTH_FORM, time=2)

    def go_to_search_field(self):
        return self.find_element(Locators.SEARCH_FIELD, time=2)

    def check_top_header(self):
        return self.find_element(Locators.TOP_HEADER)

    def check_bottom_header(self):
        return self.find_element(Locators.BOTTOM_HEADER)

    def check_main_menu(self):
        return self.find_element(Locators.MAIN_MENU)

    def check_advantages(self):
        return self.find_element(Locators.ADVANTAGES)

    def check_left_side(self):
        return self.find_element(Locators.LEFT)

    def check_main_content(self):
        return self.find_element(Locators.MAIN_CONTENT)

    def check_basket_info(self):
        element = self.find_element(Locators.BASKET_INFO)
        return element.text

    def click_add_to_basket(self):
        return self.find_element(Locators.ADD_PRODUCT_TO_BASKET).click()

    def check_confirmation_window(self):
        return self.find_element(Locators.CONFIRMATION_ADDING_TO_BASKET)

    def close_confirmation_window(self):
        return self.find_element(Locators.CLOSE_ON_CONFIRMATION_WINDOW).click()


