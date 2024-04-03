#Add/Remove Elements
from selenium.webdriver.common.by import By

link = 'https://the-internet.herokuapp.com/add_remove_elements/'

def test_add(browser):
    browser.implicitly_wait(5)
    browser.get(link)
    addelements = browser.find_element(By.CSS_SELECTOR, "#content > div > button")
    addelements.click()
    addelements.click()
    addelements.click()
    delelements = browser.find_element(By.CSS_SELECTOR, "#elements > button:nth-child(2)")
    delelements.click()
