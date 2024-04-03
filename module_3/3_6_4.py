from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import pytest
import unittest

@pytest.mark.parametrize('lesson', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
class Test_answer():
    def test_guest_should_see_login_link(self, browser, lesson):
        link = f'https://stepik.org/lesson/{lesson}/step/1'
        browser.implicitly_wait(10)
        browser.get(link)
        (WebDriverWait(browser, 20). until(EC.element_to_be_clickable((By.CLASS_NAME, "st-link_style_button"))))
        browser.find_element(By.CLASS_NAME, "st-link_style_button").click()
        input1 = browser.find_element(By.ID, "id_login_email")
        input1.send_keys("")
        input2 = browser.find_element(By.ID, "id_login_password")
        input2.send_keys("")
        signinbutton = browser.find_element(By.CLASS_NAME, "button_with-loader")
        signinbutton.click()
        answer = math.log(int(time.time() + 0.6))
        print(answer)
        answerfield = browser.find_element(By.CLASS_NAME, "string-quiz__textarea")
        answerfield.send_keys(answer)
        (WebDriverWait(browser, 20).
         until(EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))))
        submbttn = browser.find_element(By.CLASS_NAME, "submit-submission")
        submbttn.click()
        correctansw = browser.find_element(By.CLASS_NAME, "lesson__hint")
        print(correctansw.text)
        assert correctansw.text == "Correct!", "что-то пошло не так"