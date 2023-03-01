from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    element_x = browser.find_element(By.ID, 'input_value')
    x = element_x.text
    y = calc(x)
    print(y)
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)
    button1 = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button1)
    button1.click()
    input2 = browser.find_element(By.ID, 'robotCheckbox')
    input2.click()
    input3 = browser.find_element(By.ID, 'robotsRule')
    input3.click()
    button = browser.find_element(By.CLASS_NAME, 'btn-primary')
    button.click()

finally:
    time.sleep(10)
    browser.quit()