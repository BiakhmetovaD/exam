from time import sleep

from pages.form_page import FormPage
import allure


@allure.feature('Form fill')
def test_form_fill(browser):
    form_page = FormPage(browser)
    form_page.fill_form()
    sleep(3)