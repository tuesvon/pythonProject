import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://stepik.org/lesson/236895/step/1"
@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test...")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser

class TestMainPage1():
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.ID, "ember33").click()