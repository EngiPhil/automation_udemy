import unittest
from SeleniumAutomation.BimPoint.src.utility.drivers import driver_manager as driverManager
from SeleniumAutomation.BimPoint.src.utility.driver_actions import SeleniumDriver
from selenium.webdriver.common.by import By
from SeleniumAutomation.BimPoint.src.pages.element import BaseElement

class DriverActionsTest(unittest.TestCase):
    """
    This is a test to test basic methods and classes like driver_manager and pages
    """
    driver = SeleniumDriver(driverManager(browser="chrome").getWebDriver())
    agree_button = BaseElement((By.ID, "L2AGLb"))

    def test_print(self):
        print(self.driver)

    def test_getUrl(self):
        self.driver.getUrl(url_address="https://www.google.com/search?q=python")

    def test_getElement(self):
        pass

    def test_SendText(self):
        pass

    @unittest.skip("For now")
    def test_clickButton(self):
        self.driver.getUrl(url_address="https://www.google.com/search?q=python")
        self.driver.clickElement((By.ID, "L2AGLb"))

    def test_clickButton2(self):
        self.driver.getUrl(url_address="https://www.google.com/search?q=python")
        self.driver.clickElement(element=self.agree_button)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == "__main__":
    unittest.main()
