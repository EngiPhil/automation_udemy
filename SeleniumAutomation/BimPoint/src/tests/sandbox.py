from SeleniumAutomation.BimPoint.src.utility.drivers import driver_manager as driverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import SeleniumAutomation.BimPoint.src.pages.pythonorg_page as page
from SeleniumAutomation.BimPoint.src.utility.drivers import driver_manager as driverManager
from SeleniumAutomation.BimPoint.src.pages import own_page
import inspect

#tested_url = "http://www.python.org"
tested_url = "https://uat1-app.bim-point.com"

driver = driverManager(browser="chrome").getWebDriver()
driver.get(tested_url)
main_page = own_page.LoginPage(driver)
main_page.username_text_element = "test"
time.sleep(3)
main_page.continue_button_element
time.sleep(3)

print(inspect.stack())

"""

main_page.search_text_element = "pycon"
main_page.click_go_button()
search_results_page = page.SearchResultsPage(driver)



driver.find_element(By.ID, "L2AGLb").click()

WebDriverWait(driver, timeout=10).until(lambda driver: driver.find_element(By.NAME, "q"))
driver.find_element(By.NAME, "q").send_keys("BimPoint")

WebDriverWait(driver, timeout=10).until(lambda driver: driver.find_element(By.NAME, "btnK"))
driver.find_element(By.NAME, "btnK").click()

time.sleep(3)"""

