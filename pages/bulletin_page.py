from selenium.webdriver.common.by import By

from pages.base_page import BasePage

bulletin_button = (By.XPATH, '//*[@id="js-header"]/header/section/nav/ul/li[6]/a')


class BulletinPage(BasePage):
    def bulletin(self):
        self.ru_page()
        self.agree()
        self.find(bulletin_button).click()