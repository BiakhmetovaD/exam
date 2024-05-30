from selenium.webdriver.common.by import By

from pages.base_page import BasePage

live_button = (By.ID, 'adb-header-live')


class LivePage(BasePage):
    def live(self):
        self.ru_page()
        self.agree()
        self.find(live_button).click()
        trend_button = self.find((By.XPATH, '//span[@class="c-barre-now__dot u-padding-start-2"]'))
        assert trend_button.is_displayed()
