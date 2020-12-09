from selenium.webdriver.common.by import By
from lib.pages.base_page import WordPressBasePage
from lib.pages.sub_pages.search_data_elements import SearchDataElements


class NewProduct(WordPressBasePage):
    MENU_PAGES = (By.ID, 'menu-posts-product')
    NEW_PRODUCT = (By.LINK_TEXT, 'Añadir nuevo')
    WPBODY = (By.ID, 'wpbody')
    TITLE = (By.ID, 'title')
    CONTENT_IFR = (By.ID, 'content_ifr')
    CONTENT_BODY = (By.ID, 'tinymce')
    TAXONOMY_PRODUCT = (By.ID, 'taxonomy-product_cat')
    PRODUCT_CAT = (By.ID, 'in-product_cat-234')
    PRODUCT_TAG = (By.ID, 'new-tag-product_tag')
    INPUT = (By.CLASS_NAME, 'button.tagadd')
    PUBLISH = (By.ID, 'publish')
    ALL_PAGES = (By.LINK_TEXT, 'Todos los productos')
    POST_SEARCH_INPUT = (By.ID, 'post-search-input')
    SEARCH_SUBMIT = (By.ID, 'search-submit')
    TABLE_ROWS_SELECTOR = (By.XPATH, '//*[@id="the-list"]/tr')
    ROW = '//*[@id="the-list"]/'
    COLUMN = '/td[2]/strong/a'

    def access_product(self):
        self.click_button(self.MENU_PAGES)
        self.click_button(self.NEW_PRODUCT)

    def add_new_product(self, tag_name):

        title = 'Prod'+self.random_letter(10)
        self.wait_selector_visible(self.WPBODY)
        self.fill_text_field(self.TITLE, title)
        self.driver.switch_to.frame(self.driver.find_element(*self.CONTENT_IFR))
        self.fill_text_field(self.CONTENT_BODY, self.random_letter(80))
        self.driver.switch_to.default_content()
        self.wait_selector_visible(self.TAXONOMY_PRODUCT)
        self.click_button(self.PRODUCT_CAT)
        self.fill_text_field(self.PRODUCT_TAG, tag_name)
        self.click_button(self.INPUT)
        self.window_scroll_home()
        self.send_enter_key(self.PUBLISH)

        return title

    def confirm_data_product(self, product_name):

        search_web = SearchDataElements(self.driver)
        search_web.visible_selector = self.WPBODY
        search_web.all_entries = self.ALL_PAGES
        search_web.visible_search = self.WPBODY
        search_web.user_search_input = self.POST_SEARCH_INPUT
        search_web.search_submit = self.SEARCH_SUBMIT
        search_web.table_rows_selector = self.TABLE_ROWS_SELECTOR
        search_web.row = self.ROW
        search_web.column = self.COLUMN
        found = search_web.get_element(product_name)
        return found
