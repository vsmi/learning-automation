from pages.MainPage import MainPage
import pytest


@pytest.mark.skip
def test_auth_form_is_available(browser):
    main_page = MainPage(browser)
    main_page.go_to_site()
    main_page.click_on_the_login_button()
    auth_form = main_page.check_auth_form()
    assert auth_form


class TestSearch:
    def test_search_field_is_exist(self, browser):
        main_page = MainPage(browser)
        main_page.go_to_site()
        search_field = main_page.go_to_search_field()
        assert search_field

    def test_correct_search_on_main_page(self, browser):
        main_page = MainPage(browser)
        main_page.go_to_site()
        main_page.enter_word("автокресло")
        main_page.click_on_the_search_button()
        products_list = main_page.check_search_result()
        assert len(products_list) > 0

    @pytest.mark.xfail(reason="feature doesn't work")
    def test_incorrect_search_on_main_page(self, browser):
        main_page = MainPage(browser)
        main_page.go_to_site()
        main_page.enter_word("fdnjrhtckj")
        main_page.click_on_the_search_button()
        products_list = main_page.check_search_result()
        assert len(products_list) > 0
