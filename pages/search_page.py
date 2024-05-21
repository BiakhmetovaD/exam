from selenium.webdriver.common.by import By

from pages.base_page import BasePage


search_field = (By.XPATH, '//input[@class="c-search-form__input awesomplete"]')
search_button = (By.XPATH, '//button[@class="c-search-form__button"]')


class SearchPage(BasePage):
    def search(self):
        self.ru_page()
        self.agree()
        self.send_keys(search_field, 'Казахстан')
        self.find(search_button).click()
        search = self.find((By.ID, 'listing-search-autocomplete'))
        assert search.is_displayed()



