from time import sleep

from pages.just_in_page import JustInPage
import allure


def test_just_in(browser):
    just_in_page = JustInPage(browser)
    just_in_page.just_in()
    sleep(5)
