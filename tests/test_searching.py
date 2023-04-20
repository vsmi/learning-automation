from pages.MainPage import MainPage
import pytest


#@pytest.mark.skip
class TestSearch:
    def test_search_field_is_exist(self, browser):
        main_page = MainPage(browser)
        main_page.go_to_site()
        search_field = main_page.go_to_search_field()
        assert search_field

    @pytest.mark.xfail(reason="some kind of prams are in product list because it interacts with car seats")
    def test_correct_search_on_main_page(self, browser):
        main_page = MainPage(browser)
        main_page.go_to_site()
        main_page.enter_word("автокресло")
        main_page.click_on_the_search_button()
        products_list = main_page.check_search_result()
        search_flag = True
        for item in products_list:
            if "автокресло" not in item:
                search_flag = False
                break
        assert len(products_list) > 0
        assert search_flag

    @pytest.mark.xfail(reason="feature doesn't work")
    def test_incorrect_search_on_main_page(self, browser):
        main_page = MainPage(browser)
        main_page.go_to_site()
        main_page.enter_word("fdnjrhtckj")
        main_page.click_on_the_search_button()
        products_list = main_page.check_search_result()
        assert len(products_list) > 0
