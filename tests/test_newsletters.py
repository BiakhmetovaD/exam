from time import sleep

from pages.newsletters_page import NewslettersPage
import allure


def test_newsletters(browser):
    newsletters_page = NewslettersPage(browser)
    newsletters_page.newsletters()
    sleep(5)