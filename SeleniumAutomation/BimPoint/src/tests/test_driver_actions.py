import unittest
from SeleniumAutomation.BimPoint.src.utility.drivers import driver_manager as driverManager
from SeleniumAutomation.BimPoint.src.utility.driver_actions import SeleniumDriver

class DriverActionsTest(unittest.TestCase):
    """
    This is a test to test basic methods and classes like driver_manager and pages
    """
    # classmeethod?
    def setUp(self):
        print('setup')
        self.driver = SeleniumDriver(driverManager(browser="chrome").getWebDriver())

    def test_example(self):
        print("Test")

    def test_getUrl(self):
        self.driver.getUrl(url_address="http://www.python.org")


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
