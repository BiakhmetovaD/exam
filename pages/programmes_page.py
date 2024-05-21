from selenium.webdriver.common.by import By

from pages.base_page import BasePage

programmes_menu = (By.XPATH, '//*[@id="js-header"]/header/section/nav/ul/li[3]/a/span')
all_programm_button = (By.XPATH, '//*[@id="js-header"]/header/section/nav/div/div[7]/a')
dubai_button = (By.XPATH, '//*[@id="abe-2167506-title-pos1-c_program_card-"]/a')


class ProgrammesPage(BasePage):
    def programmes(self):
        self.ru_page()
        self.agree()
        self.find(programmes_menu).click()
        self.find(all_programm_button).click()
        self.find(dubai_button).click()
        image = self.find((By.XPATH, '//*[@id="js-article-header-pc"]/a/img'))
        assert image.is_displayed()

