from selenium.webdriver.support.ui import WebDriverWait


class BasePageElement(object):

    def __set__(self, obj, value):
        """Method for setting text in the <input> elements"""
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda d: driver.find_element(*self.locator)
        )
        driver.find_element(*self.locator).clear()
        driver.find_element(*self.locator).send_keys(value)

    def __get__(self, obj, owner):
        """Method for getting """
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda d: driver.find_element(*self.locator)
        )
        element = driver.find_element(*self.locator).clear()
        return element.get_attribute("value")

    def click_button(self, obj):
        """Method for clicking element"""
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda d: driver.find_element(*self.locator)
        )
        driver.find_element(*self.locator).click()
