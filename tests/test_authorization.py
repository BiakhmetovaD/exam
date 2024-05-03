import pages.authorization_page as auth
from time import sleep


def test_authorization(browser):
    authorization_page = auth.AuthorizationPage(browser)
    authorization_page.authentication_test()
    sleep(3)
