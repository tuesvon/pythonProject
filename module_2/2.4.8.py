#задание: ожидание нужного текста

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"
browser.maximize_window()

try:
    browser.get(link)
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), "$100"))
    button = browser.find_element(By.ID, 'book').click()

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    element_x = browser.find_element(By.ID, 'input_value')
    x = element_x.text
    y = calc(x)
    browser.find_element(By.ID, 'answer').send_keys(y)
    submit = browser.find_element(By.ID, 'solve')
    submit.click()
    alert = browser.switch_to.alert
    alert_text = alert.text
    pr = alert.text.split(': ')
    print(pr)

finally:
    browser.quit()


