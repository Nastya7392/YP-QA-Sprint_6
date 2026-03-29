import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

import src.urls as urls


@pytest.fixture(scope="function")
def driver():
    options = Options()
    browser_driver = webdriver.Firefox(options=options)
    browser_driver.maximize_window()
    browser_driver.get(urls.MAIN_PAGE_URL)
    yield browser_driver
    browser_driver.quit()
