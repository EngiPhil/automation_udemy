from SeleniumAutomation.BimPoint.src.utility import log_decorator
from SeleniumAutomation.BimPoint.src.utility import log
from selenium.webdriver.support.ui import WebDriverWait
from traceback import print_stack
from selenium.webdriver.common.by import By


class SeleniumDriver(object):

    def __init__(self, driver, log_file_name='selenium_log', log_file_dir=''):
        """
        A Class with driver actions for handling the pages.
        :param driver: using selenium webdriver; using a Class webdriver_manager
        :param log_file_name: name for logfile without suffix; suffix = .log
        :param log_file_dir: full pathfile, where to save the logfile; default_path = c:/logs_dir/.log
        """
        self.driver = driver
        # log file name and directory which we want to keep
        self.log_file_name = log_file_name
        self.log_file_dir = log_file_dir
        # Initializing logger object to write custom logs
        self.logger_obj = log.get_logger(log_file_name=self.log_file_name, log_sub_dir=self.log_file_dir)

    @log_decorator.log_decorator()
    def getUrl(self, url_address):
        """
        Driver gets to provided url address webpage
        :param url_addres: web url address e.g. "http://www.python.org"
        :return:
        """
        try:
            self.driver.get(url_address)
        except:
            self.logger_obj.info("Cant get to following url address " + url_address)
            raise

    @log_decorator.log_decorator()
    def getElement(self, locator):
        """
        Driver finds an element by provided locator. This method is used by many following methods, which target some element
        :param locator: is html location of the element on the page. Locator object is a tuple,
         where 1st argument provides locator type and 2nd locator name e.g. (By.ID, 'submit').
        :return: element of the webpage
        """
        element = None
        WebDriverWait(self.driver, 10).until(
            lambda d: self.driver.find_element(*locator)
        )
        try:
            element = self.driver.find_element(*locator)
            self.logger_obj.info("Element found with locatorType: " + locator[0].upper() +
                                 " and  locator: " + locator[1])
        except:
            self.logger_obj.info("Element not found with locatorType: " + locator[0].upper() +
                                 " and locator: " + locator[1])
        return element

    @log_decorator.log_decorator()
    def sendKeys(self, data, locator, element=None):
        """
        Send keys to an element -> MODIFIED
        :param data: text to be send into the textfield
        :param locator: 1st argument provides locator type and 2nd locator name e.g. (By.ID, 'submit')
        :param element: can be provided instead of locator, by default None
        :return: None
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator)
            element.send_keys(data)
            self.logger_obj.info("Sent data on element with locatorType: " + locator[0].upper() +
                                 " locatorType: " + locator[1])
        except:
            self.logger_obj.info("Cannot send data on the element with locatorType: " + locator[0].upper() +
                                 " locatorType: " + locator[1])
            print_stack()

    @log_decorator.log_decorator()
    def clickElement(self, locator=False, element=None):
        """
        Clicks on element by given locator
        :param locator: 1st argument provides locator type and 2nd locator name e.g. (By.ID, 'submit')
        :param element: can be provided instead of locator, by default None
        :return:
        """
        try:
            if locator:
                element = self.getElement(locator)
            element.click()
        except:
            #raise
            print_stack()

    @log_decorator.log_decorator()
    def close(self):
        """To close the driver"""
        self.driver.close()
