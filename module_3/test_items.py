from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_add_to_basket(browser):
    browser.get(link)
    btntobasket = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")
    assert btntobasket, "не нашёл кнопку"
    print(browser.find_element(By.CLASS_NAME, "btn-add-to-basket").text) #чтобы не добавлять time.sleep(30)
