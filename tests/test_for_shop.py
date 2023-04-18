from pages.MainPage import MainPage


def test_for_shop(browser):
    main_page = MainPage(browser)
    main_page.go_to_site()
    main_page.click_on_the_login_button()
    auth_form = main_page.check_auth_form()
    assert auth_form


def test_search_field_is_exist(browser):
    main_page = MainPage(browser)
    main_page.go_to_site()
    search_field = main_page.go_to_search_field()
    assert search_field


def test_search_on_main_page(browser):
    main_page = MainPage(browser)
    main_page.go_to_site()
    main_page.enter_word("автокресло")
    main_page.click_on_the_search_button()
    products_list = main_page.check_search_result()
    assert len(products_list) > 0

