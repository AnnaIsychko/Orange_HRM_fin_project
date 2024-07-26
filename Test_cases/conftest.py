import pytest
from selenium import webdriver
from Test_data import credentials_valid
@pytest.fixture
def setup_browser():
    driver = webdriver.Chrome() # This function sets up the browser before the test and yields it to the test function
    driver.get(credentials_valid.url)
    driver.maximize_window()
    yield driver  # This is the value that will be returned to the test function
    driver.quit()  # This will be executed after the test has finished




