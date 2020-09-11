

def test_pass(browser):

    assert browser.find_element_by_css_selector(".btn.btn-lg.btn-primary.btn-add-to-basket")
