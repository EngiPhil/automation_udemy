from SeleniumAutomation.BimPoint.src.utility.drivers import driver_manager as driverManager
import pytest

tested_url = "https://www.google.com/"

def test_chrome_driver():
    driver = driverManager(browser="chrome").getWebDriver()
    driver.get(tested_url)
    driver.quit()

def test_firefox_driver():
    driver = driverManager(browser="firefox").getWebDriver()
    driver.get(tested_url)
    driver.quit()

def test_edge_driver():
    driver = driverManager(browser="edge").getWebDriver()
    driver.get(tested_url)
    driver.quit()
