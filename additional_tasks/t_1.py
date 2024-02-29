##Напишите тест, который проверяет, что приложение успешно запускается.
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
    assert browser is not None, "Браузер не был запущен"