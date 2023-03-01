from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
browser.maximize_window()
link = 'http://suninjuly.github.io/alert_accept.html'

try:
    browser.get(link)
    browser.find_element(By.CLASS_NAME, "btn-primary").click()
    browser.switch_to.alert.accept()


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    element_x = browser.find_element(By.ID, 'input_value')
    x = element_x.text
    y = calc(x)
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)
    browser.find_element(By.CLASS_NAME, "btn-primary").click()
    alert = browser.switch_to.alert
    alert_text = alert.text
    pr = alert.text.split(': ')
    print(pr)

finally:
    browser.quit()
