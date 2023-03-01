import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
time.sleep(5)
driver.get("https://stepik.org/lesson/25969/step/12")
time.sleep(5)
textarea = driver.find_element(By.CSS_Selector, ".submit-submission")
submit_button.click()
time.sleep(5)
driver.quit()