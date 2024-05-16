from time import sleep

from pages.form_page import FormPage
from pages.search_page import SearchPage
from pages.newsletters_page import NewslettersPage
from pages.programmes_page import ProgrammesPage
from pages.weather_page import WeatherPage
from pages.just_in_page import JustInPage
from pages.bulletin_page import BulletinPage
from pages.live_page import LivePage

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
    weather_page = WeatherPage(browser)
    weather_page.weather()
    weather_page.fahrenheit()
    weather_page.your_cities()
    weather_page.my_weather()
    sleep(5)


def test_just_in(browser):
    just_in_page = JustInPage(browser)
    just_in_page.just_in()
    sleep(5)


def test_bulletin(browser):
    bulletin_page = BulletinPage(browser)
    bulletin_page.bulletin()
    sleep(5)


def test_live(browser):
    live_page = LivePage(browser)
    live_page.live()
    sleep(5)