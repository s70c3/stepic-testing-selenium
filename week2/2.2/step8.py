from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_name("firstname").send_keys("test")
    browser.find_element_by_name("lastname").send_keys("test")
    browser.find_element_by_name("email").send_keys("test")

    file = browser.find_element_by_name("file")

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    print(os.path.abspath(__file__))
    print(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'step8.txt')           # добавляем к этому пути имя файла

    file.send_keys(file_path)

    browser.find_element_by_tag_name("button").click()
finally:
    time.sleep(5)
    browser.quit()
