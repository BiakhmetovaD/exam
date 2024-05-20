from time import sleep

from pages.bulletin_page import BulletinPage
import allure


def test_bulletin(browser):
    bulletin_page = BulletinPage(browser)
    bulletin_page.bulletin()
    sleep(5)