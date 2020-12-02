from selenium.webdriver.common.by import By
from lib.pages.base_page import WordPressBasePage


class NewPages(WordPressBasePage):
    MENU_PAGES = (By.ID, 'menu-pages')
    NEW_PAGE = (By.ID, 'Añadir nueva')
    WPBODY = (By.ID, 'wpbody')
    TITLE = (By.ID, 'title')

    def access_page(self):
        self.click_button(self.MENU_PAGES)
        self.click_button(self.NEW_PAGE)

    def add_new_page(self):
        self.wait_selector_visible(self.WPBODY)
