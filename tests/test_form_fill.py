from time import sleep

from pages.form_page import FormPage
import allure


@allure.feature('Form fill')
def test_form_fill(browser):
    with allure.step('Open browser and go to site'):
        form_page = FormPage(browser)
    with allure.step('Open browser and go to site'):
        form_page.fill_form()
    sleep(3)