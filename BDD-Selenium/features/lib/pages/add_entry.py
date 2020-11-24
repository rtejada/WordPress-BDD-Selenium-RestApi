from lib.pages.base_page import WordPressBasePage
from selenium.webdriver.common.by import By
from lib.pages.sub_pages.finding_results import SearchByValue
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
    CATEGORY_PARENT = (By.ID, 'newcategory_parent')
    POST_TAG = (By.ID, 'new-tag-post_tag')
    PUBLISH = (By.ID, 'publish')

    TAG_SEARCH_INPUT = (By.ID, 'tag-search-input')
    SEARCH_INPUT = (By.ID, 'search-submit')
    TABLE_ROWS_SELECTOR = (By.XPATH, '//*[@id="the-list"]/tr')
    ROW = '//*[@id="the-list"]/'
    COLUMN = '/td[1]/strong/a'

    PATH = os.getcwd() + "/BDD-Selenium/features/lib/data/images/"

    def entry_access(self):
        self.click_button(self.POTS)
        self.wait_selector_visible(self.ENTRY)
        self.click_button(self.ENTRY)

    def add_new_entry(self, values):

        entry_name = self.random_letter(8)+str(randint(1, 100000))
        self.fill_text_field(self.TITLE, entry_name)
        self.click_button(self.MEDIA_BUTTON)
        self.wait_selector_visible(self.SCREEN_MEDIA)
        self.click_button(self.ADD_FILE)
        self.driver.find_element(*self.UPLOAD).send_keys(self.PATH + values["img"])
        self.wait_selector_visible(self.INSERT_ENTRY)
        self.wait_button_clickable(self.INSERT_ENTRY)
        self.click_button(self.INSERT_ENTRY)
        self.driver.switch_to.frame(self.driver.find_element(*self.IFRAME))
        self.fill_text_field(self.BODY_CONTENT, self.random_letter(30))
        self.driver.switch_to.default_content()
        self.wait_button_clickable(self.CATEGORY_PARENT)
        self.fill_select_by_text(self.CATEGORY_PARENT, values["categoria"])
        self.fill_text_field(self.POST_TAG, values['etiqueta'])
        self.window_scroll_home()
        self.send_enter_key(self.PUBLISH)
        return entry_name

    def confirm_category_data(self, tag_name):

        search_web = SearchByValue(self.driver)
        search_web.visible_selector = self.BODY_CONTENT
        search_web.user_search_input = self.TAG_SEARCH_INPUT
        search_web.search_submit = self.SEARCH_INPUT
        search_web.table_rows_selector = self.TABLE_ROWS_SELECTOR
        search_web.row = self.ROW
        search_web.column = self.COLUMN
        found = search_web.get_value(tag_name)
        return found



