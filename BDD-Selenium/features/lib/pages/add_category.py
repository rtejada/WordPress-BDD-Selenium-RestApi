from lib.pages.base_page import WordPressBasePage
from selenium.webdriver.common.by import By
from lib.pages.sub_pages.finding_results import SearchByValue
from random import randint
import os


class CreateCategories(WordPressBasePage):

    POTS = (By.ID, 'menu-posts')
    CATEGORY = (By.LINK_TEXT, 'Categorías')
    TAG_NAME = (By.ID, 'tag-name')
    TAG_SLUG = (By.ID, 'tag-slug')
    SUPERIOR_CATEGORY = (By.ID, 'parent')
    TAG_DESCRIPTION = (By.ID, 'tag-description')
    SUBMIT = (By.ID, 'submit')
    BODY_CONTENT = (By.ID, 'wpbody-content')
    TAG_SEARCH_INPUT = (By.ID, 'tag-search-input')
    SEARCH_INPUT = (By.ID, 'search-submit')
    TABLE_ROWS_SELECTOR = (By.XPATH, '//*[@id="the-list"]/tr')
    ROW = '//*[@id="the-list"]/'
    COLUMN = '/td[1]/strong/a'

    def category_access(self):
        self.click_button(self.POTS)
        self.wait_selector_visible(self.CATEGORY)
        self.click_button(self.CATEGORY)

    def add_category(self):

        category_name = self.random_letter(5)+str(randint(1, 100000))
        self.fill_text_field(self.TAG_NAME, category_name)
        self.fill_text_field(self.TAG_SLUG, self.random_letter(3)+str(randint(1, 100000)))
        self.fill_select_by_text(self.SUPERIOR_CATEGORY, os.getenv("SUPERIOR_CATEGORY"))
        self.fill_text_field(self.TAG_DESCRIPTION, self.random_letter(30))
        self.send_enter_key(self.SUBMIT)
        return category_name

    def confirm_data_create_category(self, tag_name):

        search_web = SearchByValue(self.driver)
        search_web.visible_selector = self.BODY_CONTENT
        search_web.user_search_input = self.TAG_SEARCH_INPUT
        search_web.search_submit = self.SEARCH_INPUT
        search_web.table_rows_selector = self.TABLE_ROWS_SELECTOR
        search_web.row = self.ROW
        search_web.column = self.COLUMN
        found = search_web.get_value(tag_name)
        return found



