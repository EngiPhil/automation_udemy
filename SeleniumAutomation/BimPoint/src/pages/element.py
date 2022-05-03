from selenium.webdriver.support.ui import WebDriverWait


class BasePageElement(object):

    def __init__(self, locator):
        self.locator = locator

    def __set__(self, obj, value):
        """Method for setting text in the <input> elements"""
        driver = obj.driver
        WebDriverWait(driver, 10).until(
            lambda d: driver.find_element(*self.locator)
        )
        driver.find_element(*self.locator).clear()
        driver.find_element(*self.locator).send_keys(value)

    def __get__(self, obj, owner):
        """Method for getting """
        driver = obj.driver
        WebDriverWait(driver, 10).until(
            lambda d: driver.find_element(*self.locator)
        )
        element = driver.find_element(*self.locator)
        return element.get_attribute("value")

    def click_button(self, obj):
        """Method for clicking element"""
        driver = obj.driver
        WebDriverWait(driver, 10).until(
            lambda d: driver.find_element(*self.locator)
        )
        driver.find_element(*self.locator).click()


class BaseElement(object):

    def __init__(self, locator):
        self.locator = locator

    def __set__(self, obj, value):
        """Method for setting text in the <input> elements"""
        driver = obj.driver
        WebDriverWait(driver, 10).until(
            lambda d: driver.getElementgetElement(self.locator)
        )
        driver.getElement(self.locator).clear()
        driver.getElement(self.locator).send_keys(value)

    def __get__(self, obj, owner):
        """Method for getting """
        driver = obj.driver
        WebDriverWait(driver, 10).until(
            lambda d: driver.getElement(self.locator)
        )
        element = driver.getElement(self.locator)
        return element.get_attribute("value")

