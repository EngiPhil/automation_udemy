import SeleniumAutomation.BimPoint.src.utility.drivers as drivers
#import pytest


chrome = drivers.driver_manager(browser="chrome")
print(chrome)

chrome.get("google.com")


