from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from time import sleep

from pages.base_page import BasePage

language_button = (By.ID, 'toggle-menu')
russian_button = (By.XPATH, 'ru-RU')
login_button = (By.ID, 'js-c-internal-links__login')
username_field = (By.XPATH, 'username')
password_field = (By.XPATH, 'password')
login_button_2 = (By.XPATH, 'Войти')


class AuthorizationPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://www.euronews.com/')

    def language_button(self):
        return self.find(language_button)

    def language_button_click(self):
        return self.language_button().click()

    def russian_button(self):
        return self.find(russian_button)

    def russian_button_click(self):
        return self.russian_button().click()

    def login_button(self):
        return self.find(login_button)

    def login_button_click(self):
        return self.login_button().click()

    def username(self):
        return self.find(username_field)

    def username_click(self):
        return self.username().click()

    def username_send(self):
        return self.username().send_keys('lipofo4377@eryod.com')

    def password(self):
        return self.find(username_field)

    def password_click(self):
        return self.password().click

    def password_send(self):
        return self.password().send_keys('Aa12345?')

    def login_button_2(self):
        return self.find(login_button_2)

    def login_button_2_click(self):
        return self.login_button_2().click()












