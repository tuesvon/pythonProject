#Basic Auth
from selenium.webdriver.common.by import By

link = 'https://admin:admin@the-internet.herokuapp.com/basic_auth'

def test_basicauth(browser):
    browser.implicitly_wait(5)
    browser.get(link)
    success = browser.find_element(By.CSS_SELECTOR, "#content > div > p")
    assert success.text == "Congratulations! You must have the proper credentials.", "Что-то пошло не так"


