from selenium.webdriver.common.by import By
from lib.pages.base_page import WordPressBasePage
from lib.pages.sub_pages.finding_results import SearchByValue


class NewProductTag(WordPressBasePage):
    MENU_PAGES = (By.ID, 'menu-posts-product')
    NEW_TAG = (By.LINK_TEXT, 'Etiquetas')
    WPBODY = (By.ID, 'wpbody')
    TAG_NAME = (By.ID, 'tag-name')
    TAG_SLUG = (By.ID, 'tag-slug')
    TAG_DESCRIPTION = (By.ID, 'tag-description')
    SUBMIT = (By.ID, 'submit')
    BODY_CONTENT = (By.ID, 'wpbody-content')
    TAG_SEARCH_INPUT = (By.ID, 'tag-search-input')
    SEARCH_INPUT = (By.ID, 'search-submit')
    TABLE_ROWS_SELECTOR = (By.XPATH, '//*[@id="the-list"]/tr')
    ROW = '//*[@id="the-list"]/'
    COLUMN = '/td[1]/strong/a'

    def access_page(self):
        self.click_button(self.MENU_PAGES)
        self.click_button(self.NEW_TAG)

    def add_tags(self):

        tag_name = 'Eti-'+self.random_letter(10)

        self.wait_selector_visible(self.WPBODY)
        self.fill_text_field(self.TAG_NAME, tag_name)
        self.fill_text_field(self.TAG_SLUG, self.random_letter(7))
        self.fill_text_field(self.TAG_DESCRIPTION, self.random_letter(20))
        self.send_enter_key(self.SUBMIT)
        return tag_name

    def confirm_data_tags(self, tag_name):

        search_web = SearchByValue(self.driver)
        search_web.visible_selector = self.BODY_CONTENT
        search_web.user_search_input = self.TAG_SEARCH_INPUT
        search_web.search_submit = self.SEARCH_INPUT
        search_web.table_rows_selector = self.TABLE_ROWS_SELECTOR
        search_web.row = self.ROW
        search_web.column = self.COLUMN
        found = search_web.get_value(tag_name)
        return found
