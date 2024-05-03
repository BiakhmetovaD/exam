from selenium import webdriver

from selenium.webdriver.common.by import By
from time import sleep
from pages.authorization_page import AuthorizationPage


def test_authorization(browser):
    authorization_page = AuthorizationPage(browser)
    authorization_page.open()
    sleep(2)
    authorization_page.language_button()
    sleep(1)
    authorization_page.language_button_click()
    authorization_page.russian_button()
    authorization_page.russian_button_click()
    sleep(1)
    authorization_page.login_button()
    authorization_page.login_button_click()
    sleep(1)
    authorization_page.username()
    authorization_page.username_click()
    sleep(1)
    authorization_page.username_send()
    sleep(1)
    authorization_page.password()
    sleep(1)
    authorization_page.password_click()
    sleep(1)
    authorization_page.password_send()
    sleep(1)
    authorization_page.login_button_2()
    sleep(1)
    authorization_page.login_button_2_click()













