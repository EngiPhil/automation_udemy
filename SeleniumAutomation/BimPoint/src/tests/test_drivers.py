import unittest
from SeleniumAutomation.BimPoint.src.utility.drivers import driver_manager as driverManager

tested_url = "https://www.google.com/"


class PythonOrgSearch(unittest.TestCase):
    """
    Test for driver_manager class
    Testing drivers of main web-browser providers: Chrome, FireFox, Edge
    """

    def test_chrome_driver(self):
        driver = driverManager(browser="chrome").getWebDriver()
        driver.get(tested_url)
        driver.quit()

    def test_firefox_driver(self):
        driver = driverManager(browser="firefox").getWebDriver()
        driver.get(tested_url)
        driver.quit()

    def test_edge_driver(self):
        driver = driverManager(browser="edge").getWebDriver()
        driver.get(tested_url)
        driver.quit()


if __name__ == "__main__":
    unittest.main()
