import unittest
from SeleniumAutomation.BimPoint.src.utility.drivers import driver_manager as driverManager
from SeleniumAutomation.BimPoint.src.pages import pythonorg_page as page
import HtmlTestRunner


class HtmlTestResultTest(unittest.TestCase):
    """
    This is a test to test HtmlTestRunners, which provides test report in html format
    """
    # classmeethod?
    def setUp(self):
        self.driver = driverManager(browser="chrome").getWebDriver()
        self.driver.get("http://www.python.org")

    def test_example(self):
        print("Test")
        main_page = page.MainPage(self.driver)
        main_page.search_text_element = "pycon"
        main_page.click_go_button()
        search_results_page = page.SearchResultsPage(self.driver)
        # Verifies that the results page is not empty
        self.assertTrue(search_results_page.is_results_found(), "No results found.")

    def test_search_in_python_org(self):
        """Tests python.org search feature. Searches for the word "pycon" then
        verified that some results show up.  Note that it does not look for
        any particular text in search results page. This test verifies that
        the results were not empty."""

        #Load the main page. In this case the home page of Python.org.
        main_page = page.MainPage(self.driver)
        #Checks if the word "Python" is in title
        self.assertTrue(main_page.is_title_matches(), "python.org title doesn't match.")
        #Sets the text of search textbox to "pycon"
        main_page.search_text_element = "pycon"
        main_page.click_go_button()
        search_results_page = page.SearchResultsPage(self.driver)
        #Verifies that the results page is not empty
        self.assertTrue(search_results_page.is_results_found(), "No results found.")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=r"C:\Users\FilipV\Filip\PyCharm\BimPoint\src\reports"))
