import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_basket_button_is_presented(browser):
    browser.get(link)
    time.sleep(10)
    elements = browser.find_elements_by_class_name("btn-add-to-basket")
    assert len(elements)>0, "No 'Add to basket' button presented"
