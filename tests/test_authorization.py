from time import sleep

from pages.authorization_page import AuthorizationPage
import allure


@allure.feature('Authorization')
def test_authorization(browser):
    authorization_page = AuthorizationPage(browser)
    with allure.step('Open browser and go to site'):
        authorization_page.home_page()
    with allure.step('Authenticate '):
        authorization_page.authenticate()




