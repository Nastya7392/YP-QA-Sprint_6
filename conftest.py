import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

import src.data as data


@pytest.fixture(scope="function")
def driver():
    options = Options()
    browser_driver = webdriver.Firefox(options=options)
    browser_driver.maximize_window()
    browser_driver.get(data.main_page_url)
    yield browser_driver
    browser_driver.quit()
