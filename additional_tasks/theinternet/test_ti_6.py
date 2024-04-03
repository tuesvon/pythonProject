from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = 'https://the-internet.herokuapp.com/context_menu'



def test_context(browser):
    browser.get(link)
    WebDriverWait(browser,5).until(EC.element_to_be_clickable((By.ID, "hot-spot")))
    context = browser.find_element(By.ID, "hot-spot")
    action = ActionChains(browser)
    action.context_click(context).perform()
    WebDriverWait(browser,5).until(EC.alert_is_present())
    alert = browser.switch_to.alert
    alert_text = alert.text
    assert alert_text == "You selected a context menu", "что-то пошло не так"
    alert.accept()
