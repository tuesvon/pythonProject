from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

link = "http://stage-teplo.phoenixit.ru/login"

browser = webdriver.Chrome()
browser.maximize_window()
browser.get(link)

# Ваш код, который заполняет обязательные поля
browser.switch_to().alert().dismiss()
print('нажал на кнопку "Отмена"')
time.sleep(10)
input1 = browser.find_element(By.ID, "login")
input1.send_keys("administrator")



