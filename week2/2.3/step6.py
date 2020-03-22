from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")

    browser.find_element_by_tag_name("button").click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element_by_id("input_value").text

    browser.find_element_by_id("answer").send_keys(str(calc(x)))

    browser.find_element_by_tag_name("button").click()

finally:
    time.sleep(5)
    browser.quit()

