import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="session")
def browser():
    service = Service(executable_path='./chromedriver')
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

