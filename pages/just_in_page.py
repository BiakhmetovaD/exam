from selenium.webdriver.common.by import By

from pages.base_page import BasePage

just_in_button = (By.XPATH, '//*[@id="js-header"]/header/section/nav/ul/li[5]/a')


class JustInPage(BasePage):
    def just_in(self):
        self.ru_page()
        self.agree()
        self.find(just_in_button).click()
        trend_button = self.find((By.XPATH, '//*[@id="enw-main-content"]/section[1]/ul/li[1]/strong'))
        assert trend_button.is_displayed()
