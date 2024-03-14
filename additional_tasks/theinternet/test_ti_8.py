from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

link = 'https://the-internet.herokuapp.com/disappearing_elements'


@pytest.fixture
def browserChrome():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


def test_elements(browser):
    browser.get(link)
    elements1 = browser.find_elements(By.TAG_NAME, "li")
    print(len(elements1), " - количество элементов до обновления страницы")
    while True: 
        browser.refresh()
        WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.TAG_NAME, "li")))
        elements2 = browser.find_elements(By.TAG_NAME, "li")
        print(len(elements2), " - количество элементов после обновления страницы")
        if len(elements1) != len(elements2):
            break
            assert len(elements2) != len(elements1), "что-то пошло не так"