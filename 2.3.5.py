from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/redirect_accept.html'

try:
    browser.get(link)
    browser.maximize_window()
    button = browser.find_element(By.CLASS_NAME, 'btn-primary')
    time.sleep(1)
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    element_x = browser.find_element(By.ID, 'input_value')
    x = element_x.text
    y = calc(x)
    print(y)
    time.sleep(1)
    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(y)
    browser.find_element(By.CLASS_NAME, 'btn-primary').click()
    time.sleep(1)
    alert = browser.switch_to.alert
    alert_text = alert.text
    pr = alert.text.split(': ')
    print(pr)

finally:
    time.sleep(2)
    browser.quit()
