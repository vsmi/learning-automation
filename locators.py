from selenium.webdriver.common.by import By


class Locators:
    LOGIN_BTN = (By.CLASS_NAME, "HRegistrationAndAuthLink")
    AUTH_FORM = (By.CLASS_NAME, "CommonWData")
    SEARCH_FIELD = (By.ID, "search_string")
    SEARCH_BTN = (By.CLASS_NAME, "BtnReset.CommonBtn")
    PRODUCTS_LIST = (By.CLASS_NAME, "ProductsList")
    STUB = "stub"

