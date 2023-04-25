from pages.MainPage import MainPage
from pages.ConfirmationWindow import ConfirmationWindow


class TestBasket:
    def test_basket_is_empty(self, browser):
        main_page = MainPage(browser)
        main_page.go_to_site()
        info = main_page.check_basket_info()
        assert info == 'пуста'

    def test_add_product_to_basket(self, browser):
        main_page = MainPage(browser)
        cw = ConfirmationWindow(browser)
        main_page.go_to_site()
        main_page.go_to_search_field()
        main_page.enter_word('автокресло')
        main_page.click_on_the_search_button()
        main_page.click_add_to_basket()
        cw.check_confirmation_window()
        cw.close_confirmation_window()
        info = main_page.check_basket_info()
        assert info != 'пуста'