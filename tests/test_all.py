from time import sleep

from pages.form_page import FormPage
from pages.search_page import SearchPage
from pages.newsletters_page import NewslettersPage
from pages.programmes_page import ProgrammesPage
from pages.weather_page import WeatherPage


def test_form_fill(browser):
    form_page = FormPage(browser)
    form_page.fill_form()
    sleep(3)


def test_search(browser):
    search_page = SearchPage(browser)
    search_page.search()
    sleep(5)


def test_newsletters(browser):
    newsletters_page = NewslettersPage(browser)
    newsletters_page.newsletters()
    sleep(5)


def test_programmes(browser):
    programmes_page = ProgrammesPage(browser)
    programmes_page.programmes()
    sleep(5)

def test_weather(browser):
