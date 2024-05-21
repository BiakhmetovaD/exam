from selenium.webdriver.common.by import By

from pages.base_page import BasePage

programmes_menu = (By.XPATH, '//li[@class="js-programs_links list-item list-item--programs"]')
all_programm_button = (By.XPATH, '//a[@class="c-link-chevron u-text-weight-bold u-text-transform-uppercase "]')
dubai_button = (By.XPATH, '//a[@class="m-object__title__link   "]')


class ProgrammesPage(BasePage):
    def programmes(self):
        self.ru_page()
        self.agree()
        self.find(programmes_menu).click()
        self.find(all_programm_button).click()
        self.find(dubai_button).click()
        image = self.find((By.XPATH, '//img[@class="c-article-pc-disclaimer__partner__img"]'))
        assert image.is_displayed()

