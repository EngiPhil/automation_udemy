from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

#Relative path was not working. Solution: https://stackoverflow.com/questions/37636268/pycharm-does-not-see-files-in-relative-path-with
#Run->Edit Configurations - Working directory changed from C:\Users\FilipV\Filip\PyCharm\Automation1\SeleniumAutomation to C:\Users\FilipV\Filip\PyCharm\Automation1

driver_path = "SeleniumAutomation/drivers/chromedriver_100-0-4896.exe"
driver = webdriver.Chrome(driver_path)

driver.get('https://orteil.dashnet.org/cookieclicker/')
driver.implicitly_wait(10)

cookie = driver.find_element(By.ID, "bigCookie")
cookie_count = driver.find_element(By.ID, "cookies")
items = [driver.find_element(By.ID, "productPrice" + str(i)) for i in range(1, -1, -1)]

actions = ActionChains(driver)

for i in range(5000):
    actions.click(cookie)
    actions.perform()
    count = int(cookie_count.text.split(" ")[0])
    for item in items:
        value = int(item.text)
        if value <= count:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.double_click()
            upgrade_actions.perform()
