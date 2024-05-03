from selenium.webdriver.common.by import By

from pages.base_page import BasePage

language_button = (By.XPATH, '//button[@class="c-menu-language__btn u-cursor-pointer u-text-weight-bold js-menu-language__btn"]')
russian_button = (By.XPATH, '//a[@lang="ru-RU"]')
login_button = (By.ID, 'adb-header-login')
username_field = (By.ID, 'gigya-loginID-83718878221439220')
password_field = (By.ID, 'gigya-password-124357688285627710')
auth_button = (By.XPATH, '//*[@id="gigya-login-form"]/div[2]/div[1]/div[5]/input')


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

        username = self.find(username_field)
        username.click()
        username.send_keys('lipofo4377@eryod.com')
        password = self.find(password_field)
        password.click()
        password.send_keys('Aa12345?')

        self.find(auth_button).click()
