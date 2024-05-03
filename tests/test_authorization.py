from time import sleep

from pages.form_page import FormPage
from pages.search_page import SearchPage


def test_form_fill(browser):
    form_page = FormPage(browser)
    form_page.authenticate()
    form_page.fill_form()
    sleep(3)


def test_search(browser):
    search_page = SearchPage(browser)
    search_page.search()
    sleep(3)
