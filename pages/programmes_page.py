from selenium.webdriver.common.by import By

from pages.base_page import BasePage

programmes_menu = (By.XPATH, '//li[@class="js-programs_links list-item list-item--programs"]')
all_programmes_button = (By.XPATH, '//a[@class="c-link-chevron u-text-weight-bold u-text-transform-uppercase "]')
dubai_button = (By.XPATH, '//a[@href="/business/2023/01/17/foreign-investors-help-to-drive-a-property-boom-in-dubai"]')


class ProgrammesPage(BasePage):
    def programmes(self):
        self.home_page()
        self.agree()
        self.find(programmes_menu).click()
        all_programmes = self.find(all_programmes_button)
        self.browser.execute_script("arguments[0].scrollIntoView();", all_programmes)
        all_programmes.click()
        dubai = self.find(dubai_button)
        self.browser.execute_script("arguments[0].scrollIntoView();", dubai)
        dubai.click()
        image = self.find((By.XPATH, '//img[@class="c-article-pc-disclaimer__partner__img"]'))
        assert image.is_displayed()

