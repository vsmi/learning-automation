from pages.MainPage import MainPage
from pages.OneClickWindow import OneClickWindow
import pytest

class TestForms:
    def test_forms_valid(self, browser):
        main_page = MainPage(browser)
        ocw = OneClickWindow(browser)
        main_page.go_to_site()
        main_page.go_to_search_field()
        main_page.enter_word('автокресло')
        main_page.click_on_the_search_button()
        main_page.click_one_click_button()
        name = ocw.enter_name('Victoria')
        email = ocw.enter_email('test@mail.com')
        phone = ocw.enter_phone('9100001122')
        main_page.click_one_click_window()
        class_value_of_name = ocw.check_valid(name)
        class_value_of_email = ocw.check_valid(email)
        class_value_of_phone = ocw.check_valid(phone)
        assert "Control_Valid" in class_value_of_name
        assert "Control_Valid" in class_value_of_email
        assert "Control_Valid" in class_value_of_phone

    @pytest.mark.xfail(reason="there is no validation on name field")
    def test_forms_name_invalid(self, browser):
        main_page = MainPage(browser)
        ocw = OneClickWindow(browser)
        main_page.go_to_site()
        main_page.go_to_search_field()
        main_page.enter_word('автокресло')
        main_page.click_on_the_search_button()
        main_page.click_one_click_button()
        name = ocw.enter_name('')
        email = ocw.enter_email('test@mail.com')
        phone = ocw.enter_phone('9100001122')
        main_page.click_one_click_window()
        class_value_of_name = ocw.check_valid(name)
        class_value_of_email = ocw.check_valid(email)
        class_value_of_phone = ocw.check_valid(phone)
        assert "Control_Invalid" in class_value_of_name
        assert "Control_Valid" in class_value_of_email
        assert "Control_Valid" in class_value_of_phone



