from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/cats.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_id("button")
finally:
    time.sleep(4)
    browser.quit()