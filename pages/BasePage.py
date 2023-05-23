from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://obninsk-kolyaski.ru/"
        self.main_window = driver.current_window_handle

    def find_element(self, locator, time=10):
        """
        Ищет элемент и возвращает его
        """
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator), \
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        """
        Ищет элементы и возвращает их в виде списка
        """
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator), \
                                                      message=f"Can't find elements by locator {locator}")

    def go_to_site(self):
        """
        Вызывает функцию get из webdriver, переходит на указанную страницу
        """
        return self.driver.get(self.base_url)

    def switch_to_confirmation_window(self, locator):
        """
        Переключается на окно
        """
        return self.driver.switch_to.window(self.locator)

    def go_to_back(self):
        self.driver.back()

    def get_attribute_of_elem(self, elem):
        return elem.get_attribute('class')




