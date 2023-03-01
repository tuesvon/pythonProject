from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = 'http://suninjuly.github.io/selects1.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.maximize_window()
    x = browser.find_element(By.ID, 'num1').text
    y = browser.find_element(By.ID, 'num2').text
    sum_el = int(x) + int(y)
    print(sum_el)
    browser.find_element(By.CLASS_NAME, 'custom-select').click()
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text('%s' % sum_el)

    button = browser.find_element(By.CLASS_NAME, 'btn-default')
    button.click()

finally:
    time.sleep(10)
    browser.quit()