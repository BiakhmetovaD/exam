from selenium.webdriver.common.by import By

from pages.base_page import BasePage

live_button = (By.ID, 'js-menu-live-desktop')


class LivePage(BasePage):
    def live(self):
        self.ru_page()
        self.agree()
        self.find(live_button).click()
        trend_button = self.find((By.XPATH, '//*[@id="enw-main-content"]/section[2]/ul/li[1]/strong'))
        assert trend_button.is_displayed()
