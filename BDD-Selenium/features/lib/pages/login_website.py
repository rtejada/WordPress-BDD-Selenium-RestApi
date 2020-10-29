from selenium.webdriver.common.by import By
from lib.pages.base_page import WordPressBasePage
import os


class LoginWebsite(WordPressBasePage):

    USER_LOGIN = (By.ID, 'user_login')
    USER_PASS = (By.ID, 'user_pass')
    SUBMIT = (By.ID, 'wp-submit')

    URL_WORDPRESS = ''
    LOGIN = ''
    PASSWORD = ''

    def __init__(self, driver):

        super().__init__(driver)
        self.load_variables()

    def load_variables(self):
        self.URL_WORDPRESS = os.getenv('URL_WORDPRESS')
        self.LOGIN = os.getenv('USER_WORDPRESS')
        self.PASSWORD = os.getenv('PASS_WORDPRESS')

    def load_page(self):
        self.driver.get(self.URL_WORDPRESS)

    def enter_page(self):

        self.fill_text_field(self.USER_LOGIN, self.LOGIN)

        self.fill_text_field(self.USER_PASS, self.PASSWORD)

        self.click_button(self.SUBMIT)
