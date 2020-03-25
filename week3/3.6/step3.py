import time
import math
import pytest
from selenium import webdriver




@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('lesson', ["236895", "236896","236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, lesson):
    link = f"https://stepik.org/lesson/{lesson}/step/1"
    browser.get(link)

    answer = math.log(int(time.time()))
    browser.find_element_by_class_name("string-quiz__textarea").send_keys(str(answer))
    browser.find_element_by_class_name("submit-submission").click()
    assert browser.find_element_by_class_name("smart-hints__hint").text == "Correct!", "Time isn't correct"



