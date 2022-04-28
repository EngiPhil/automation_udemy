from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.options import Options as EdgeOptions


class driver_manager():
    """
    Class for creating a webdriver instance
    :arg
    -browser - specify web-browser; chrome choosen as default
    """
    def __init__(self, browser="chrome"):
        self.browser = browser

    def getWebDriver(self):
        if self.browser == "chrome":
            options = ChromeOptions()
            service = ChromeService(executable_path=ChromeDriverManager().install())
            driver = webdriver.Chrome(options=options, service=service)
        elif self.browser == "firefox":
            options = FirefoxOptions()
            service = FirefoxService(executable_path=GeckoDriverManager().install())
            driver = webdriver.Chrome(options=options, service=service)
        elif self.browser == "edge":
            options = EdgeOptions()
            service = EdgeService(executable_path=EdgeChromiumDriverManager().install())
            driver = webdriver.Chrome(options=options, service=service)

        return driver