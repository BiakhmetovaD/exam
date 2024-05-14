from selenium.webdriver.common.by import By

from pages.base_page import BasePage

weather_button = (By.XPATH, '//*[@id="js-header"]/header/section/nav/ul/li[4]/a/svg')
city_field = (By.XPATH, '//*[@id="weather-search-addtomyweather"]/div[1]/div/input')
search_button = (By.XPATH, '//*[@id="weather-search-addtomyweather"]/button')


class WeatherPage(BasePage):
    def weather(self):
        self.ru_page()
        self.find(weather_button).click()
        self.find(city_field).click()
        self.send_keys(city_field, 'Нур-Султан')
        self.find(search_button).click()