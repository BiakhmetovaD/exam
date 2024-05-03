from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from time import sleep

from pages.base_page import BasePage

fist_name_field = (By.XPATH, 'profile.firstName')
last_name_field = (By.XPATH, 'profile.lastName')
wom = (By.ID, 'gigya-multiChoice-0-107849046191306260')
men = (By.ID, 'gigya-multiChoice-1-107849046191306260')
country = (By.XPATH, 'profile.country')
update = (By.XPATH, 'Обновить профиль')


class AddingData(BasePage):
    def firs_name(self):
        return self.find(fist_name_field)

    def first_name_click(self):
        return self.firs_name().click

    def first_name_send(self):
        return self.firs_name().send_keys('Test')

    def last_name(self):
        return self.find(last_name_field)

    def last_name_click(self):
        return self.last_name().click

    def last_name_send(self):
        return self.last_name().send_keys('Test')

    def gender(self):
        pass



