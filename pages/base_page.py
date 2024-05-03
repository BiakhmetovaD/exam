from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:
    def __init__(self, browser: WebDriver):
        self.browser = browser

    def find(self, args):
        self.sleep()
        return self.browser.find_element(*args)

    def find_elements(self, args):
        self.sleep()
        return self.browser.find_elements(*args)

    def sleep(self):
        self.browser.implicitly_wait(10)
