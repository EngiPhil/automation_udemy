from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver_path = "C:\\Filip\\Pycharm Projects\\automation_udemy\\SeleniumAutomation\\drivers\\chromedriver_100-0-4896.exe"
driver = webdriver.Chrome(driver_path)

driver.get('https://www.techwithtim.net/')

link = driver.find_element(By.LINK_TEXT, "Python Programming")
link.click()

try:
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
    )

    element.click()
    print("click Beginner")

    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "sow-button-19310003"))
    )

    element.click()
    print('Click Get Started')

    driver.back()
    print('Back')
    driver.back()
    driver.back()
    print('Back')
    driver.forward()
    driver.forward()

except:
    print('Except ')
    driver.quit()
