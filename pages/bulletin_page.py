from selenium.webdriver.common.by import By

from pages.base_page import BasePage

bulletin_button = (By.XPATH, '//a[@title="Выпуск новостей"]')


class BulletinPage(BasePage):
    def bulletin(self):
        self.ru_page()
        self.agree()
        self.find(bulletin_button).click()
        trend_button = self.find((By.XPATH, '//span[@class="c-barre-now__dot u-padding-start-2"]'))
        assert trend_button.is_displayed()
