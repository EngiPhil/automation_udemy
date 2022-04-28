from SeleniumAutomation.BimPoint.src.pages.locators import MainPageLocators
from SeleniumAutomation.BimPoint.src.pages.element import BasePageElement
from selenium.webdriver.common.by import By


class BasePage(object):
    """Base class to initialize the base page that will be called from all
    pages"""

    def __init__(self, driver):
        self.driver = driver


class LoginPage(BasePage):
    """Home page action methods come here. I.e. Python.org"""

    # Declares a variable that will contain the retrieved text
    search_text_element = SearchTextElement()

