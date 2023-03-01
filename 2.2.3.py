from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = ''

try:
    browser = webdriver.Chrome()
    browser.get(link)

finally:
    time.sleep(10)
    browser.quit()