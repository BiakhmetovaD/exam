from time import sleep
from selenium.webdriver.common.by import By

from pages.base_page import BasePage

language_button = (By.XPATH, '//button[@class="c-menu-language__btn u-cursor-pointer u-text-weight-bold js-menu-language__btn"]')
russian_button = (By.XPATH, '//a[@lang="ru-RU"]')
login_button = (By.ID, 'adb-header-login')
username_field = (By.ID, 'gigya-loginID-83718878221439220')
password_field = (By.ID, 'gigya-password-124357688285627710')
auth_button = (By.XPATH, '//input[@value="Войти"]')


class AuthorizationPage(BasePage):
    def home_page(self):
        self.browser.get('https://www.euronews.com/')

    def authenticate(self):
        self.home_page()
        self.agree()
        self.find(language_button).click()
        self.find(russian_button).click()

        self.agree()
        self.find(login_button).click()

        self.send_keys(username_field, 'lipofo4377@eryod.com')
        self.send_keys(password_field, 'Aa12345?')

        self.find(auth_button).click()
        self.find((By.ID, 'gigya-textbox-firstName'))

