from selenium.webdriver.common.by import By

from pages.base_page import BasePage

live_button = (By.XPATH, '//*[@id="js-menu-live-desktop"]')


class LivePage(BasePage):
    def live(self):
        self.ru_page()
        self.agree()
        self.find(live_button).click()