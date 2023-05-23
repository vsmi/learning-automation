from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.MainPage import MainPage
import pytest


#@pytest.mark.skip
class TestMainPage:
    def test_auth_form_is_available(self, browser):
        main_page = MainPage(browser)
        main_page.go_to_site()
        main_page.click_on_the_login_button()
        auth_form = main_page.check_auth_form()
        assert auth_form

    def test_check_top_header_is_exist(self, browser):
        main_page = MainPage(browser)
        main_page.go_to_site()
        top_header = main_page.check_top_header()
        assert top_header, "there is no top header"

    def test_check_bottom_header_is_exist(self, browser):
        main_page = MainPage(browser)
        main_page.go_to_site()
        bottom_header = main_page.check_bottom_header()
        assert bottom_header, "there is no bottom header"

    def test_check_main_menu_is_exist(self, browser):
        main_page = MainPage(browser)
        main_page.go_to_site()
        main_menu = main_page.check_main_menu()
        assert main_menu, "there is no main menu"

    def test_check_advantages_is_exist(self, browser):
        main_page = MainPage(browser)
        main_page.go_to_site()
        advantages = main_page.check_advantages()
        assert advantages, "there is no advantages"

    def test_check_left_side_is_exist(self, browser):
        main_page = MainPage(browser)
        main_page.go_to_site()
        left_side = main_page.check_left_side()
        assert left_side, "there is no left side"

    def test_check_main_content_is_exist(self, browser):
        main_page = MainPage(browser)
        main_page.go_to_site()
        main_content = main_page.check_main_content()
        assert main_content, "there is no main content"


class TestF:
    def test_main_menu_clickable(self, browser):
        main_page = MainPage(browser)
        main_page.go_to_site()
        main_menu_items = len(main_page.find_main_menu_items())
        f = True
        for i in range(main_menu_items):
            try:
                menu_item = main_page.find_main_menu_items()[i]
                menu_item.click()
                main_page.go_to_previous_page()
                main_menu_items = main_page.find_main_menu_items()
            except Exception:
                f = False
        assert f

