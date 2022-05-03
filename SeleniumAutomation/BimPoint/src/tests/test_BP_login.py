import unittest
from SeleniumAutomation.BimPoint.src.utility.drivers import driver_manager as driverManager
from SeleniumAutomation.BimPoint.src.pages import pythonorg_page as page


class PythonOrgSearch(unittest.TestCase):

    # setUpClass(cls) = run once for the whole class (together with @classmeethod)
    # setUp(self) = run before every method

    def setUp(self):
        print('setup')
        self.driver = driverManager(browser="chrome").getWebDriver()
        self.driver.get("https://uat1-app.bim-point.com/")

    def test_login_successful(self):
        """Tests uat1-app.bim-point.com app login feature. Pass username of test user and click Continue button.
        After that text field for password should appear and password of test user will be provided.
        Clicking on Login button, test user should be logged in."""

        # Load the login page.
        main_page = page.MainPage(self.driver)
        # Check the title of login page
        # Provide the username
        # Click Continue
        # Provide the password
        # Click Login
        # Check list of projects

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
