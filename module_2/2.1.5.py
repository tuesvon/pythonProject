import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

#выполнение условий задачи
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)
    input2 = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    input2.click()
    input3 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    input3.click()
    print(y)

#нажатие на кнопку submit
    button = browser.find_element(By.CLASS_NAME, 'btn-default')
    button.click()
finally:
    time.sleep(5)
    browser.quit()