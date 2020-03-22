from selenium import webdriver
import time

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/execute_script.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element_by_id("input_value").text
    y = calc(x)
    answer = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
    answer.send_keys(y)
    browser.find_element_by_id("robotCheckbox").click()
    browser.find_element_by_id("robotsRule").click()

    browser.find_element_by_tag_name("button").click()

except Exception as error:
    print(error)


finally:
    time.sleep(5)
    browser.quit()
