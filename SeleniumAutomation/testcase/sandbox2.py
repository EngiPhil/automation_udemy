from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.relative_locator import locate_with
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
import time

options = ChromeOptions()
service = ChromeService(executable_path=ChromeDriverManager().install())

driver = webdriver.Chrome(service=service, options=options)

# Navigate to url
driver.get("http://www.google.com")

WebDriverWait(driver, 100).until(
    lambda driver: driver.find_element(By.ID, "L2AGLb")
)

#driver.find_element(By.ID, "L2AGLb").click()

more_info = driver.find_element(locate_with(By.TAG_NAME, "button").near({By.ID: "L2AGLb"}))
print(more_info)
more_info.click()

time.sleep(22)

WebDriverWait(driver, 100).until(
    lambda driver: driver.find_element(By.NAME, "q")
)

# Enter "webdriver" text and perform "ENTER" keyboard action
driver.find_element(By.NAME, "q").send_keys("webdriver" + Keys.ENTER)

# Perform action ctrl + A (modifier CONTROL + Alphabet A) to select the page
webdriver.ActionChains(driver).key_down(Keys.CONTROL).send_keys("a").perform()
