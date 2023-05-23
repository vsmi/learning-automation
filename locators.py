from selenium.webdriver.common.by import By


class MainPageLocators:
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
    ADD_PRODUCT_TO_BASKET = (By.CSS_SELECTOR, ".PIToPutInABasket [data-product_id='790']")
    BASKET_ON_MAIN_PAGE = (By.CSS_SELECTOR, "[id='HBasket']")
    BASKET_INFO = (By.CSS_SELECTOR, "#HBasket span")
    MM_ITEM = (By.CSS_SELECTOR, ".MMItems.FlexBox.FlexBox_CenterAlignment")
    MM_ITEMS = (By.XPATH, "//div[@class='MMItems FlexBox FlexBox_CenterAlignment']/div")
    ONECLICK = (By.CLASS_NAME, "PIPurchaseOneClick")
    ONECLICKW = (By.CLASS_NAME, "CommonWData")


class ConfirmationWindowLocators:
    CONFIRMATION_ADDING_TO_BASKET = (By.ID, "ConfirmationOnAdditionOfGoodsInBasket")
    CLOSE_CONFIRMATION_WINDOW = (By.CLASS_NAME, "CommonWCloseBtn")
    COUNTER = (By.CSS_SELECTOR, ".Amount .InputMask_Int")
    TO_INCREASE_COUNT = (By.CLASS_NAME, "ToIncreaseCount")
    PRICE_AND_COUNT = (By.CLASS_NAME, "PriceAndCount")
    TO_BASKET = (By.CSS_SELECTOR, ".CommonBorderBtn.CommonSolidBorderBtn")


class BasketLocators:
    BASKET = (By.ID, "BasketCart")


class OneClickLocators:
    NAME = (By.ID, "fname47")
    EMAIL = (By.ID, "email49")
    PHONE = (By.ID, "phone50")
    SUBMIT = (By.CSS_SELECTOR, "[title='Подтвердить оформление заказа']")




