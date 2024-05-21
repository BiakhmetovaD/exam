from selenium.webdriver.common.by import By

from pages.authorization_page import AuthorizationPage

newsletters_button = (By.XPATH, '//span[@data-event="newsletter-link-header"]')
choose_button = (By.XPATH, '//label[@class="block w-full btn-tertiary unchecked-label cursor-pointer"]')
email_field = (By.XPATH, '//input[@class="w-full"]')
continue_button = (By.XPATH, '//input[@class="btn-primary mt-6 md:mt-0 cursor-pointer block w-full md:inline-block"]')
checkbox = (By.ID, 'subs-checkbox-travel_en')
update_button = (By.XPATH, '//input[@value="Обновить мои рассылки"]')


class NewslettersPage(AuthorizationPage):
    def newsletters(self):
        self.authenticate()
        self.ru_page()
        self.find(newsletters_button).click()
        self.find(choose_button).click()
        self.find(email_field).click()
        self.send_keys(email_field, 'lipofo4377@eryod.com')
        self.find(continue_button).click()
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        self.find(checkbox).click()
        self.find(update_button).click()
        image = self.find((By.ID, 'gigya-profile-form'))
        assert image.is_displayed()



