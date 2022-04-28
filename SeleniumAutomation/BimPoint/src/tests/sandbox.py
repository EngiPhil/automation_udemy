from SeleniumAutomation.BimPoint.src.utility.drivers import driver_manager as driverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
import SeleniumAutomation.BimPoint.src.pages.pythonorg_page as page
from SeleniumAutomation.BimPoint.src.utility.drivers import driver_manager as driverManager
from SeleniumAutomation.BimPoint.src.pages import pythonorg_page

tested_url = "http://www.python.org"

driver = driverManager(browser="chrome").getWebDriver()
driver.get(tested_url)
main_page = page.MainPage(driver)
main_page.search_text_element = 'Pycon'



ele = driver.page_source
print(ele)
time.sleep(1)
button = main_page
main_page.click_button()
time.sleep(2)
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

