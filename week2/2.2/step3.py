from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = int(browser.find_element_by_id("num1").text)
    num2 = int(browser.find_element_by_id("num2").text)

    sum = str(num1+num2)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(sum)

    browser.find_element_by_class_name("btn").click()

# except Exception as err:
#     print(err)
finally:
    time.sleep(5)
    browser.quit()

