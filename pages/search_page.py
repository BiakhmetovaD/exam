from selenium.webdriver.common.by import By

from pages.base_page import BasePage


search_field = (By.XPATH, '//*[@id="search-autocomplete"]/div[1]/div/input')
search_button = (By.XPATH, '//*[@id="search-autocomplete"]/button')
news = (By.XPATH, '//*[@id="abe-2519066-title-pos5-listing_library"]/a')


class SearchPage(BasePage):
    def search(self):
        self.ru_page()
        self.agree()

    def search_func(self):
        self.send_keys(search_field, 'Казахстан')
        self.find(search_button).click()
        self.browser.execute_script("arguments[0].scrollIntoView(true);", news)



