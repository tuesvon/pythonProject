#Checkboxes

from selenium.webdriver.common.by import By

link = 'https://the-internet.herokuapp.com/checkboxes'
def test_checkboxes(browser):
    browser.implicitly_wait(5)
    browser.get(link)
    ch1 = browser.find_element(By.CSS_SELECTOR, '#checkboxes > input:nth-child(1)')
    ch2 = browser.find_element(By.CSS_SELECTOR, '#checkboxes > input:nth-child(3)')
    ch1ch = ch1.get_attribute("checked")
    ch2ch = ch2.get_attribute("checked")
    assert ch1.get_attribute("checked") or ch2.get_attribute("checked"), "Какой-то из чекбоксов не выставлен изначально"
    print("Состояние чекбоксов после открытия страницы:")
    print("ch1:", ch1ch)
    print("ch2:", ch2ch)
    ch1.click()
    ch2.click()
    ch11checked = ch1.get_attribute("checked")
    ch22checked = ch2.get_attribute("checked")
    assert ch1.get_attribute("checked") or ch2.get_attribute("checked"), "Что-то пошло не так"
    print("Состояние после изменения статуса:")
    print("ch1:", ch11checked)
    print("ch2:", ch22checked)
