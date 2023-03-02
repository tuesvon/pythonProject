#задание про Exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
browser.maximize_window()
link = 'http://suninjuly.github.io/cats.html'

try:
    browser.get(link)
    browser.find_element(By.ID, "button")

finally:
    browser.quit()