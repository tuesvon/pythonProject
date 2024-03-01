# Напишите тест, который проверяет, что при удалении товара из корзины количество товаров уменьшается на единицу.
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link1 = "https://market.yandex.ru/"


@pytest.fixture
def browser():
    print("\nЗапуск приложения")
    browser = webdriver.Chrome()
    yield browser
    browser.quit()
    print("\nТест завершён")


def test_shopping(browser):
    browser.get(link1)
    wait = WebDriverWait(browser, 10)
    search_field = wait.until(EC.visibility_of_element_located((By.ID, "header-search")))
    search_field.send_keys("xiaomi 13")
    (browser.find_element(By.CSS_SELECTOR, "body > div.page > div > div:nth-child(3) > div:nth-child(2) > "
                                           "header > div._7ImK_ > div > div > div > div > div > div > form > div "
                                           "> button > span").click())
    browser.find_element(By.PARTIAL_LINK_TEXT, '12GB+512GB').click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    browser.find_element(By.CSS_SELECTOR, "#offerActions > div > div._1Jo-W.cia-vs.cia-cs").click()
    time.sleep(1)  # для того, чтобы появилось количество добавленных товаров
    qty = browser.find_element(By.CSS_SELECTOR, "#offerActions > div > div._1Jo-W.cia-vs.cia-cs > div > a").text
    assert qty == '1', "Что-то пошло не так"
    browser.find_element(By.CSS_SELECTOR,
                         "#offerActions > div > div._1Jo-W.cia-vs.cia-cs > div > div:nth-child(1) > button").click()
    qty = browser.find_element(By.CSS_SELECTOR, "#offerActions > div > div.NwIxC.cia-vs.cia-cs").text
    assert qty == 'Корзина', "Что-то пошло не так"
