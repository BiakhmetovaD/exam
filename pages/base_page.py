from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

agree_button = (By.ID, 'didomi-notice-agree-button')


class BasePage:
    def __init__(self, browser: WebDriver):
        self.browser = browser

    def ru_page(self):
        self.browser.get('https://ru.euronews.com/')

    def agree(self):
        self.find(agree_button).click()

    def find(self, args):
        self.sleep()
        return self.browser.find_element(*args)

    def find_elements(self, args):
        self.sleep()
        return self.browser.find_elements(*args)

    def send_keys(self, field, keys):
        field_element = self.find(field)
        field_element.click()
        field_element.send_keys(keys)

    def sleep(self):
        self.browser.implicitly_wait(10)
