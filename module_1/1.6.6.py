from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("https://eda.yandex.ru/retail/vkusvill?placeSlug=vkusvill_kadqm")
    add_button = browser.find_element(By.CSS_SELECTOR, ".add")
    add_button.click()
    browser.get("https://fake-shop.com/book2.html")
    add_button = browser.find_element(By.CSS_SELECTOR, ".add")
    add_button.click()
    browser.get("https://fake-shop.com/basket.html")
    goods = browser.find_elements(By.CSS_SELECTOR, ".good")
    assert len(goods) == 2

finally:
    time.sleep(15)
    browser.quit()