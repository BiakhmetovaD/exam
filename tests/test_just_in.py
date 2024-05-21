from time import sleep

from pages.just_in_page import JustInPage
import allure


@allure.feature('Just in')
def test_just_in(browser):
    just_in_page = JustInPage(browser)
    just_in_page.just_in()
    sleep(5)
