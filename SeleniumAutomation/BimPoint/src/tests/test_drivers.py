from SeleniumAutomation.BimPoint.src.utility.drivers import driver_manager as driverManager
import pytest

"""
Test for driver_manager class
Class for constructing selenium webdriver
Testing drivers of main web-browser providers: Chrome, FireFox, Edge
"""

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
