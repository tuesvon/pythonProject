##Напишите тест, который проверяет, что при входе на главную страницу отображается правильный заголовок.
import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    print("\nЗапуск приложения")
    browser = webdriver.Chrome()
    yield browser
    browser.quit()
    print("\nТест завершён")
def test_running(browser):
    browser.get("https://google.com")
    assert browser.title == "Google", "Заголовок страницы не соответствует результату"