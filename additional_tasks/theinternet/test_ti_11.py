#Dynamic Content
#1 - https://stackoverflow.com/questions/49900117/python-selenium-list-object-has-no-attribute-text-error
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

link = 'https://the-internet.herokuapp.com/dynamic_content'

@pytest.fixture()
def browserChrome():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

def test_content(browser):
    browser.get(link)
    elements1 = browser.find_elements(By.CLASS_NAME, "large-10.columns")
    elements1_text = [element.text for element in elements1]
    print("Тексты до обновления:")
    for text in elements1_text:
        print(text)
    browser.refresh()
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, "large-10.columns")))
    elements2 = browser.find_elements(By.CLASS_NAME, "large-10.columns")
    elements2_text = [element.text for element in elements2]
    print("\nТексты после обновления:")
    for text in elements2_text:
        print(text)
    assert elements1_text != elements2_text, "что-то пошло не так"