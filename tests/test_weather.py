from time import sleep

from pages.weather_page import WeatherPage
import allure


def test_weather(browser):
    weather_page = WeatherPage(browser)
    weather_page.weather()
    weather_page.fahrenheit()
    weather_page.your_cities()
    weather_page.my_weather()
    sleep(5)
