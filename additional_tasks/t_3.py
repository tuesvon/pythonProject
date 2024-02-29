# Напишите тест, который проверяет, что пользователь может успешно авторизоваться на сайте.

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def browser():
    print("\nЗапуск приложения")
    browser = webdriver.Chrome()
    yield browser
    browser.quit()
    print("\nТест завершён")

def test_authorization(browser):
    browser.get("https://google.com")
    wait = WebDriverWait(browser, 10)
    sign_in_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Войти")))
    sign_in_button.click()
    l_field = wait.until(EC.visibility_of_element_located((By.ID, "identifierId")))
    assert l_field.is_displayed(), "Поле ввода email отображается"
