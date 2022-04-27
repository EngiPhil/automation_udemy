from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions


class driver_manager():
    def __init__(self, browser):
        self.browser = browser

    def getWebDriver(self):
        if self.browser == "chrome":
            options = ChromeOptions()
            service = ChromeService(executable_path=ChromeDriverManager().install())
            driver = webdriver.Chrome(options=options, service=service)

        return driver