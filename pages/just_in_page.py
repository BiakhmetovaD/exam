from selenium.webdriver.common.by import By

from pages.base_page import BasePage

just_in_button = (By.XPATH, '//a[@title="Just In"]')


class JustInPage(BasePage):
    def just_in(self):
        self.home_page()
        self.agree()
        self.find(just_in_button).click()
        trend_button = self.find_elements((By.XPATH, '//span[@class="c-barre-now__dot u-padding-start-2"]'))
        assert trend_button

