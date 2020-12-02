from lib.pages.base_page import WordPressBasePage
from selenium.webdriver.common.by import By
from lib.pages.sub_pages.search_data_elements import SearchDataElements
from random import randint
import os


class CreateEntries(WordPressBasePage):

    POTS = (By.ID, 'menu-posts')
    ENTRY = (By.LINK_TEXT, 'Añadir nueva')
    TITLE = (By.ID, 'title')
    MEDIA_BUTTON = (By.ID, 'insert-media-button')
    SCREEN_MEDIA = (By.ID, '__wp-uploader-id-0')
    ADD_FILE = (By.ID, 'menu-item-upload')
    UPLOAD = (By.ID, '__wp-uploader-id-1')
    INSERT_ENTRY = (By.XPATH, '//*[@id="__wp-uploader-id-0"]/div[4]//div[2]/button')
    IFRAME = (By.ID, 'content_ifr')
    BODY_CONTENT = (By.ID, 'tinymce')
    POSTBOX_CONTAINER = (By.ID, 'postbox-container-1')
    CATEGORY_ID = (By.ID, 'in-category-103')
    NEW_TAG_POST = (By.ID, 'new-tag-post_tag')
    ADD_TAG = (By.CLASS_NAME, 'button.tagadd')
    PUBLISH = (By.ID, 'publish')

    WPBODY_CONTENT = (By.ID, 'wpbody-content')
    ALL_ENTRIES = (By.LINK_TEXT, 'Todas las entradas')
    WPBODY = (By.ID, 'wpbody')
    POST_SEARCH = (By.ID, 'post-search-input')
    SEARCH_INPUT = (By.ID, 'search-submit')
    TABLE_ROWS_SELECTOR = (By.XPATH, '//*[@id="the-list"]/tr')
    ROW = '//*[@id="the-list"]/'
    COLUMN = '/td[1]/strong/a'

    PATH = os.getcwd() + "/BDD-Selenium/features/lib/data/images/"

    def entry_access(self):
        self.click_button(self.POTS)
        self.wait_selector_visible(self.ENTRY)
        self.click_button(self.ENTRY)

    def add_new_entry(self, tag):

        entry_name = self.random_letter(8)+str(randint(1, 100000))
        self.fill_text_field(self.TITLE, entry_name)
        self.driver.switch_to.frame(self.driver.find_element(*self.IFRAME))
        self.fill_text_field(self.BODY_CONTENT, self.random_letter(70))
        self.driver.switch_to.default_content()
        self.wait_selector_visible(self.POSTBOX_CONTAINER)
        self.click_button(self.CATEGORY_ID)
        self.fill_text_field(self.NEW_TAG_POST, tag)
        self.click_button(self.ADD_TAG)
        self.window_scroll_home()
        self.send_enter_key(self.PUBLISH)
        return entry_name

    def confirm_entry_data(self, tag_name):

        search_web = SearchDataElements(self.driver)
        search_web.visible_selector = self.WPBODY_CONTENT
        search_web.all_entries = self.ALL_ENTRIES
        search_web.visible_search = self.WPBODY
        search_web.user_search_input = self.POST_SEARCH
        search_web.search_submit = self.SEARCH_INPUT
        search_web.table_rows_selector = self.TABLE_ROWS_SELECTOR
        search_web.row = self.ROW
        search_web.column = self.COLUMN
        found = search_web.get_element(tag_name)
        return found



