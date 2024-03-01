#Напишите тест, который проверяет, что при регистрации нового пользователя на сайте успешно отображается сообщение
# об успешной регистрации.

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
link = 'https://the-internet.herokuapp.com/login'
@pytest.fixture()
def browserChrome():
    print("\nЗапуск теста")
    browser = webdriver.Chrome()
    yield browser
    browser.quit()
    print("\nЗавершение теста")

def test_authc(browser):
    browser.get(link)
    login = browser.find_element(By.ID, "username")
    login.send_keys("tomsmith")
    password = browser.find_element(By.ID, "password")
    password.send_keys("SuperSecretPassword!")
    browser.find_element(By.CLASS_NAME, "radius").click()
    success = browser.find_element(By.ID, "flash-messages")
    assert 'You logged into a secure area!' in success.text, "Регистрация неуспешна"


