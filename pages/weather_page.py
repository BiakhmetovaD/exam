from selenium.webdriver.common.by import By

from pages.base_page import BasePage

weather_button = (By.XPATH, '//li[@class="c-menu-icons"]')
city_field = (By.XPATH, '//input[@data-apiurl="/api/weather/search?query="]')
search_button = (By.XPATH, '//div[@id="weather-search-addtomyweather"]/child::button[@class="c-search-form__button"]')
fahrenheit_button = (By.XPATH, '//div[@class="c-search__switch__label c-search__switch__label--degree-f js-degree js-degree-f"]')
your_cities_button = (By.ID, 'js-add-to-my-weather')
my_weather_dropdown = (By.ID, 'js-show-my-weather')


class WeatherPage(BasePage):
    def weather(self):
        self.ru_page()
        self.agree()
        self.find(weather_button).click()
        self.find(city_field).click()
        self.send_keys(city_field, 'Нур-Султан')
        self.find(search_button).click()

    def fahrenheit(self):
        self.find(fahrenheit_button).click()

    def your_cities(self):
        self.find(your_cities_button).click()

    def my_weather(self):
        self.find(my_weather_dropdown).click()
        weather_dropdown = self.find((By.ID, 'js-show-my-weather'))
        assert weather_dropdown.is_displayed()

