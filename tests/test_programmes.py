from time import sleep

from pages.programmes_page import ProgrammesPage
import allure


@allure.feature('Programmes')
def test_programmes(browser):
    programmes_page = ProgrammesPage(browser)
    programmes_page.programmes()
    sleep(5)
