from time import sleep

from pages.weather_page import WeatherPage
import allure


@allure.feature('Weather')
def test_weather(browser):
    weather_page = WeatherPage(browser)
    with allure.step('Open browser, go to site and search Nur-Sultan city'):
        weather_page.weather()
    with allure.step('Change from celsius to fahrenheit'):
        weather_page.fahrenheit()
    with allure.step('Add to your cities'):
        weather_page.your_cities()
    with allure.step('Check your cities'):
        weather_page.my_weather()
    sleep(5)
