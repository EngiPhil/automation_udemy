import SeleniumAutomation.BimPoint.src.utility.drivers as drivers
#import pytest
import time

chrome = drivers.driver_manager(browser='chrome').getWebDriver()
print(chrome)

chrome.get("http://www.python.org")
time.sleep(3)

