import pytest
from selenium import webdriver
import time


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default= None,
                     help="Choose language: ru, es")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    language = request.config.getoption("language")

    if language not in ("ru", "es"):
        browser.quit()
        raise pytest.UsageError("--language should be ru or es")
    link = f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/"
    print(link)
    browser.get(link)
    yield browser
    print("\nquit browser..")
    browser.quit()
