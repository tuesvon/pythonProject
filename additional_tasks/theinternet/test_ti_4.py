#Challenging DOM

from selenium.webdriver.common.by import By

link = 'https://the-internet.herokuapp.com/challenging_dom'

def test_challdom(browser):
    browser.get(link)
    rbutton1_tekst = browser.find_element(By.CLASS_NAME, "button.alert").text
    bbutton1_tekst = browser.find_element(By.CLASS_NAME, "button").text
    gbutton1_tekst = browser.find_element(By.CLASS_NAME, "button.success").text
    print("\nЗначения кнопок до нажатия:", rbutton1_tekst, bbutton1_tekst, gbutton1_tekst)
    successbtn = browser.find_element(By.CLASS_NAME, "button.success")
    successbtn.click()
    rbutton2_tekst = browser.find_element(By.CLASS_NAME, "button.alert").text
    bbutton2_tekst = browser.find_element(By.CLASS_NAME, "button").text
    gbutton2_tekst = browser.find_element(By.CLASS_NAME, "button.success").text
    print("\nЗначения кнопок после нажатия:", rbutton2_tekst, bbutton2_tekst, gbutton2_tekst)
    assert (rbutton1_tekst != rbutton2_tekst
            or bbutton1_tekst != bbutton2_tekst
            or gbutton1_tekst != gbutton2_tekst), "Что-то пошло не так"