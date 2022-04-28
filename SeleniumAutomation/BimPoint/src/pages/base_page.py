from SeleniumAutomation.BimPoint.src.utility.actions import BasePageElement


from selenium.webdriver.common.by import By


class MainPageLocators(object):
    GO_BUTTON = (By.ID, "submit")


class SearchResultPageLocators(object):
    pass


class SearchTextElement(BasePageElement):
    locator = "q"


class GoButtonElement(BasePageElement):
    locator = "go"


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    search_text_element = SearchTextElement()

    def is_title_matches(self):
        return "Python" in self.driver.title

    def click_go_button(self):
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        # * Splat / unpack operator f(*[2,3]) => f(2,3)
        element.click()


class SearchResultPage(BasePage):

    def is_results_found(self):
        return "No results found." not in self.driver.page_source
