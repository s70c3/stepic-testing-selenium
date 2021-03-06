import math
import time
import math

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID,"price"),"$100")
        )
    browser.find_element_by_tag_name("button").click()

    x = browser.find_element_by_id("input_value").text

    browser.find_element_by_id("answer").send_keys(str(calc(x)))

    browser.find_element_by_id("solve").click()


finally:
    time.sleep(5)
    browser.quit()

