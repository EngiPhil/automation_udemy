from SeleniumAutomation.BimPoint.src.utility.drivers import driver_manager as driverManager
#import pytest
import time

chrome = driverManager(browser='chrome').getWebDriver()
print(chrome)

chrome.get("http://www.python.org")
time.sleep(3)

