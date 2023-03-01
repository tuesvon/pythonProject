import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import os

link = 'http://suninjuly.github.io/file_input.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.NAME, 'firstname')
    input1.send_keys('Dimitrii')
    input2 = browser.find_element(By.NAME, 'lastname')
    input2.send_keys('Kanaev')
    input3 = browser.find_element(By.NAME, 'email')
    input3.send_keys('d@d.ru')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "file.txt"
    file_path = os.path.join(current_dir, file_name)
    file = browser.find_element(By.ID, 'file')
    file.send_keys(file_path)
    browser.find_element(By.CLASS_NAME, 'btn-primary').click()

finally:
    time.sleep(5)
    browser.quit()