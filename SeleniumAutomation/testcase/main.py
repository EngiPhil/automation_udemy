import unittest
from selenium import webdriver
import page

# driver_path = r"SeleniumAutomation/drivers/chromedriver_100-0-4896.exe"
driver_path = r"C:\Users\FilipV\Filip\PyCharm\Automation1\SeleniumAutomation\drivers\chromedriver_100-0-4896.exe"


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        print('setup')
        self.driver = webdriver.Chrome(driver_path)
        self.driver.get("http://www.python.org")

    def test_example(self):
        print("Test")
        assert True

    def test_example_2(self):
        print("Test 2")
        assert False

    def not_a_test(self):
        print("This wont print")

    def test_search_python(self):
        main_page = page.MainPage(self.driver)
        assert main_page.is_title_matches()
        main_page.search_text_element = "pycon"
        main_page.click_go_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_results_found()

    def test_title(self):
        main_page = page.MainPage()
        assert main_page.is_title_matches()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
