from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class test_RegForm(unittest.TestCase):
    def test_Reg1(link1):
        link1 = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link1)
        input1 = browser.find_element(By.CLASS_NAME, "form-control.first:required")
        input1.send_keys("Dimitrii")
        input2 = browser.find_element(By.CLASS_NAME, "form-control.second:required")
        input2.send_keys("Kanaev")
        input3 = browser.find_element(By.CLASS_NAME, "form-control.third:required")
        input3.send_keys("wwas@wwas.wwas")
        input4 = browser.find_element(By.XPATH, "//div[2]/div[1]/input")
        input4.send_keys("+79909664456")
        input5 = browser.find_element(By.XPATH, "//div[2]/div[2]/input")
        input5.send_keys("Saint-P")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        browser.quit()

    def test_Reg2(link2):
        link2 = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link2)
        input1 = browser.find_element(By.CLASS_NAME, "form-control.first:required")
        input1.send_keys("Dimitrii")
        input2 = browser.find_element(By.CLASS_NAME, "form-control.second:required")
        input2.send_keys("Kanaev")
        input3 = browser.find_element(By.CLASS_NAME, "form-control.third:required")
        input3.send_keys("wwas@wwas.wwas")
        input4 = browser.find_element(By.XPATH, "//div[2]/div[1]/input")
        input4.send_keys("+79909664456")
        input5 = browser.find_element(By.XPATH, "//div[2]/div[2]/input")
        input5.send_keys("Saint-P")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        browser.quit()


if __name__ == '__main__':
    unittest.main()
