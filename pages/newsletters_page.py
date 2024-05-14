from selenium.webdriver.common.by import By

from pages.base_page import BasePage


newsletters_button = (By.XPATH, '//*[@id="js-header"]/header/div[1]/ul/li[2]/a/span')
choose_button = (By.XPATH, '//*[@id="newsletters-form"]/div/div[1]/div/div[2]/label[1]')
email_field = (By.XPATH, '//*[@id="register-newsletters-form"]/div[1]/input')
continue_button = (By.XPATH, '//*[@id="register-newsletters-form"]/div[2]/input')


class NewslettersPage(BasePage):
    def newsletters(self):
        self.ru_page()
        self.agree()
        self.find(newsletters_button).click()
        self.find(choose_button).click()
        self.find(email_field).click()
        self.send_keys(email_field, 'lipofo4377@eryod.com')
        self.find(continue_button).click()



