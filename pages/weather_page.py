from selenium.webdriver.common.by import By

from pages.base_page import BasePage

weather_button = (By.XPATH, '//*[@id="js-header"]/header/section/nav/ul/li[4]/a')
city_field = (By.XPATH, '//*[@id="weather-search-addtomyweather"]/div[1]/div/input')
search_button = (By.XPATH, '//*[@id="weather-search-addtomyweather"]/button')
fahrenheit_button = (By.XPATH, '//*[@id="js-degree-selector"]/label/div[2]')
your_cities_button = (By.XPATH, '//*[@id="js-add-to-my-weather"]')
my_weather_dropdown = (By.XPATH, '//*[@id="js-show-my-weather"]')


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



