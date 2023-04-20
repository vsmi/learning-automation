from selenium.webdriver.common.by import By


class Locators:
    LOGIN_BTN = (By.CLASS_NAME, "HRegistrationAndAuthLink")
    AUTH_FORM = (By.CLASS_NAME, "CommonWData")
    SEARCH_FIELD = (By.ID, "search_string")
    SEARCH_BTN = (By.CLASS_NAME, "BtnReset.CommonBtn")
    PRODUCTS_LIST = (By.CSS_SELECTOR, ".PIName")
    TOP_HEADER = (By.CLASS_NAME, "TopHeader")
    BOTTOM_HEADER = (By.CLASS_NAME, "BottomHeader")
    MAIN_MENU = (By.CLASS_NAME, "MainMenu")
    ADVANTAGES = (By.CLASS_NAME, "AdvantagesAfterHeader")
    LEFT = (By.CLASS_NAME, "LeftAside")
    MAIN_CONTENT = (By.CLASS_NAME, "MainContent")
    STUB = "stub"

