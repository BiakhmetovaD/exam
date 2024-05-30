from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

agree_button = (By.ID, 'didomi-notice-agree-button')


class BasePage:
    def __init__(self, browser: WebDriver):
        self.browser = browser

    def home_page(self):
        self.browser.get('https://www.euronews.com/')

    def ru_page(self):
        self.browser.get('https://ru.euronews.com/')

    def agree(self):
        try:
            self.find(agree_button).click()
        except NoSuchElementException:
            pass

    def find(self, args):
        element = self.browser.find_element(*args)
        self.sleep()
        return element

    def find_elements(self, args):
        elements = self.browser.find_elements(*args)
        self.sleep()
        return elements

    def send_keys(self, input_field, keys):
        field = self.find(input_field)
        field.clear()
        field.click()
        field.send_keys(keys)

    def sleep(self):
        self.browser.implicitly_wait(10)
