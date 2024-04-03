import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    print("\nНачало теста")
    browser = webdriver.Chrome()
    yield browser
    browser.quit()
    print("\nТест завершён")