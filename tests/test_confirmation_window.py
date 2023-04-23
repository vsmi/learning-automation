from pages.MainPage import MainPage


class TestConfirmationWindow:
    def test_check_count_of_products(self, browser):
        main_page = MainPage(browser)
        main_page.go_to_site()
        main_page.go_to_search_field()
        main_page.enter_word('автокресло')
        main_page.click_on_the_search_button()
        main_page.click_add_to_basket()
        main_page.check_confirmation_window()
        main_page.to_increase_count()
        count = main_page.check_quantity_of_products()
        assert count == "2"

