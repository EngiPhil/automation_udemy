from SeleniumAutomation.BimPoint.src.pages.locators import AppLoginPageLocators as LoginLocators
from SeleniumAutomation.BimPoint.src.pages.element import BasePageElement
from selenium.webdriver.common.by import By


class BasePage(object):
    """Base class to initialize the base page that will be called from all
    pages"""

    def __init__(self, driver):
        self.driver = driver


class LoginPage(BasePage):
    """Login page for https://uat1.bim-point.com"""
    # Declares elements of the page
    # User name textfield
    username_text_element = BasePageElement(LoginLocators.USERNAME_TEXT)
    # Continue button
    continue_button_element = BasePageElement(LoginLocators.CONTINUE_BUTTON)
    # These buttons are available after providing username and clicking Continue button
    # Pasword textfield
    password_text_element = BasePageElement(LoginLocators.PASSWORD_TEXT)
    # Login button
    login_button_element = BasePageElement(LoginLocators.LOGIN_BUTTON)
