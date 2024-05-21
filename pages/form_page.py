from selenium.webdriver.common.by import By

import random
from time import sleep

from pages.authorization_page import AuthorizationPage


fist_name_field = (By.ID, 'gigya-textbox-firstName')
last_name_field = (By.ID, 'gigya-textbox-lastName')
woman_button = (By.ID, 'gigya-multiChoice-0-107849046191306260')
man_button = (By.ID, 'gigya-multiChoice-1-107849046191306260')
birth_date_field = (By.ID, 'gigya-textbox-51199175038457890')
country_field = (By.ID, 'gigya-textbox-country')
country_random = (By.XPATH, f'//*[@id="gigya-textbox-country"]/option[{random.randrange(1,244)}]')
update_button = (By.XPATH, '//*[@id="gigya-profile-form"]/div[9]/div[6]/input')


class FormPage(AuthorizationPage):
    def fill_form(self):
        self.authenticate()
        self.send_keys(fist_name_field, 'First Name Test')
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        self.send_keys(last_name_field, 'Last Name Test')

        self.change_gender()
        self.set_birth_date()
        self.set_country()
        sleep(3)
        self.find(update_button).click()
        image = self.find((By.ID, 'gigya-profile-form'))
        assert image.is_displayed()

    def change_gender(self):
        woman = self.find(woman_button)
        woman_class = woman.get_attribute('class')
        man = self.find(man_button)
        if 'gigya-empty' in woman_class:
            woman.click()
        else:
            man.click()

    def set_birth_date(self):
        day = random.randrange(1, 28)
        month = random.randrange(1, 12)
        year = random.randrange(1980, 2015)
        if day < 10:
            day = '0' + str(day)
        if month < 10:
            month = '0' + str(month)
        self.send_keys(birth_date_field, f'{month}/{day}/{year}')

    def set_country(self):
        self.find(country_field).click()
        self.find(country_random).click()
