from time import sleep

from pages.live_page import LivePage
import allure



def test_live(browser):
    live_page = LivePage(browser)
    live_page.live()
    sleep(5)