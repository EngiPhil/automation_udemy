import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def test_chrome_session():
    options = ChromeOptions()
    driver = webdriver.Chrome(options=options)

    driver.quit()


def test_edge_session():
    options = EdgeOptions()
    driver = webdriver.Edge(options=options)

    driver.quit()


def test_firefox_session():
    options = FirefoxOptions()
    driver = webdriver.Firefox(options=options)

    driver.quit()
