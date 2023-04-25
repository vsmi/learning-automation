from pages.MainPage import MainPage
from pages.ConfirmationWindow import ConfirmationWindow


class TestConfirmationWindow:
    def test_check_count_of_products(self, browser):
        main_page = MainPage(browser)
        cw = ConfirmationWindow(browser)
        main_page.go_to_site()
        main_page.go_to_search_field()
        main_page.enter_word('автокресло')
        main_page.click_on_the_search_button()
        main_page.click_add_to_basket()
        cw.check_confirmation_window()
        cw.to_increase_count()
        count = cw.check_quantity_of_products()
        assert count == "2"

