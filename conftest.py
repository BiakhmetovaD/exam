from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def browser():
    options = Options()
    options.add_argument('--headless')
    options.add_argument("window-size=1920,1080")
    chrome_browser = webdriver.Chrome(options=options)
    chrome_browser.implicitly_wait(10)
    chrome_browser.maximize_window()
    return chrome_browser
