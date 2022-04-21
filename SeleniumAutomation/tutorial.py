from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


#driver_path = '/SeleniumAutomation/drivers/chromedriver_100-0-4896.exe'
driver_path = "C:\\Filip\\Pycharm Projects\\automation_udemy\\SeleniumAutomation\\drivers\\chromedriver_100-0-4896.exe"
driver = webdriver.Chrome(driver_path)

driver.get('https://www.techwithtim.net/')
print(driver.title)

search = driver.find_element(By.NAME, "s")
search.send_keys("test")
search.send_keys(Keys.RETURN)

time.sleep(5)

driver.quit()
