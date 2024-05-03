from pages.base_page import BasePage


class SearchPage(BasePage):

    def search(self):
        self.ru_page()
        self.agree()
        print('searching')
