import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'https://the-internet.herokuapp.com/dropdown'
@pytest.fixture
def browserChrome():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


def test_dropdown(browser):
    browser.get(link)
    browser.find_element(By.ID, "dropdown").click()
    option = (browser.find_element(By.CSS_SELECTOR, "[value='2']"))
    option.click()
    print(option.text)
    attribute_selected = option.get_attribute("selected")
    assert attribute_selected is not None, "Этот вариант не выбран"