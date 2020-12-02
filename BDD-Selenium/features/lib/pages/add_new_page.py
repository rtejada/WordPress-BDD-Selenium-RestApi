from selenium.webdriver.common.by import By
from lib.pages.base_page import WordPressBasePage
from lib.pages.sub_pages.search_data_elements import SearchDataElements
from random import randint


class NewPage(WordPressBasePage):
    MENU_PAGES = (By.ID, 'menu-pages')
    NEW_PAGE = (By.LINK_TEXT, 'Añadir nueva')
    WPBODY = (By.ID, 'wpbody')
    TITLE = (By.ID, 'title')
    CONTENT_IFR = (By.ID, 'content_ifr')
    CONTENT_BODY = (By.ID, 'tinymce')
    PARENT_DIV = (By.ID, 'pageparentdiv')
    PARENT_ID = (By.ID, 'parent_id')
    PUBLISH = (By.ID, 'publish')
    ALL_PAGES = (By.LINK_TEXT, 'Todas las páginas')
    POST_SEARCH_INPUT = (By.ID, 'post-search-input')
    SEARCH_SUBMIT = (By.ID, 'search-submit')
    TABLE_ROWS_SELECTOR = (By.XPATH, '//*[@id="the-list"]/tr')
    ROW = '//*[@id="the-list"]/'
    COLUMN = '/td[1]/strong/a'

    def access_page(self):
        self.click_button(self.MENU_PAGES)
        self.click_button(self.NEW_PAGE)

    def add_new_page(self, value):
        id = '438'
        title = 'Page'+str(randint(1, 1000))+'-'+self.random_letter(7)
        self.wait_selector_visible(self.WPBODY)
        self.fill_text_field(self.TITLE, title)
        self.driver.switch_to.frame(self.driver.find_element(*self.CONTENT_IFR))
        self.fill_text_field(self.CONTENT_BODY, self.random_letter(80))
        self.driver.switch_to.default_content()
        self.wait_selector_visible(self.PARENT_DIV)
        if value == 'padre':
            self.send_enter_key(self.PUBLISH)

        else:
            self.fill_select_by_value(self.PARENT_ID, id)
            self.send_enter_key(self.PUBLISH)

        return title

    def confirm_data_page(self, tag_name):

        search_web = SearchDataElements(self.driver)
        search_web.visible_selector = self.WPBODY
        search_web.all_entries = self.ALL_PAGES
        search_web.visible_search = self.WPBODY
        search_web.user_search_input = self.POST_SEARCH_INPUT
        search_web.search_submit = self.SEARCH_SUBMIT
        search_web.table_rows_selector = self.TABLE_ROWS_SELECTOR
        search_web.row = self.ROW
        search_web.column = self.COLUMN
        found = search_web.get_element(tag_name)
        return found
