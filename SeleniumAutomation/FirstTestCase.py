from selenium import webdriver

#driver_path = '/SeleniumAutomation/drivers/chromedriver_100-0-4896.exe'
driver_path = "C:\\Filip\\Pycharm Projects\\automation_udemy\\SeleniumAutomation\\drivers\\chromedriver_100-0-4896.exe"
driver = webdriver.Chrome(driver_path)
driver.get('https://www.thetestingworld.com/testings/')

# Maximize browser

driver.maximize_window()

# Enter Data to the textbox
driver.find_element_by_name("fld_username").send_keys("helloworld")
print(driver.title)
driver.find_element_by_name("fld_username").clear()
driver.quit()
