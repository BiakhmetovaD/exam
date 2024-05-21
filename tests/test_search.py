from time import sleep

from pages.search_page import SearchPage
import allure


@allure.feature('Search')
def test_search(browser):
    search_page = SearchPage(browser)
    search_page.search()
    sleep(5)

