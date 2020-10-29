from selenium.webdriver.common.by import By
from lib.pages.base_page import WordPressBasePage
from lib.pages.sub_pages.finding_results import SearchByValue
from lib.pages.sub_pages.query_users import DataBase


class AddNewUsers(WordPressBasePage):

    MENU_ICON_USERS = (By.ID, 'menu-users')
    WPBODY_CONTENT = (By.ID, 'wpbody-content')
    ADD_NEW = (By.LINK_TEXT, 'Añadir nuevo')
    USER_LOGIN = (By.ID, 'user_login')
    EMAIL = (By.ID, 'email')
    FIRST_NAME = (By.ID, 'first_name')
    LAST_NAME = (By.ID, 'last_name')
    URL = (By.ID, 'url')
    ROLE = (By.ID, 'role')
    CREATE_USER = (By.ID, 'createusersub')
    USER_SEARCH_INPUT = (By.ID, 'user-search-input')
    SEARCH_SUBMIT = (By.ID, 'search-submit')
    TABLE_ROWS_SELECTOR = (By.XPATH, '//*[@id="wpbody-content"]//table/tbody/tr')
    ROW = '//*[@id="wpbody-content"]//table/tbody/'
    COLUMN = '/td[1]/strong/a'

    def load_user_window(self):
        self.click_button(self.MENU_ICON_USERS)
        self.wait_selector_visible(self.WPBODY_CONTENT)
        self.click_button(self.ADD_NEW)

    def new_users_data(self, user_register):
        user_name = user_register['name']+self.random_letter(7)

        self.fill_text_field(self.USER_LOGIN, user_name)
        self.fill_text_field(self.EMAIL, self.random_letter(7)+'@'+self.random_letter(5)+'.es')
        self.fill_text_field(self.FIRST_NAME, user_register['name']+self.random_letter(10))
        self.fill_text_field(self.LAST_NAME, user_register['name']+self.random_letter(8))
        self.fill_text_field(self.URL, 'www.'+self.random_letter(9)+'.es')
        self.fill_select_by_value(self.ROLE, user_register['role'])
        self.send_enter_key(self.CREATE_USER)

        return user_name

    def confirm_web_added_data(self, user_name):

        search_web = SearchByValue(self.driver)
        search_web.visible_selector = self.WPBODY_CONTENT
        search_web.user_search_input = self.USER_SEARCH_INPUT
        search_web.search_submit = self.SEARCH_SUBMIT
        search_web.table_rows_selector = self.TABLE_ROWS_SELECTOR
        search_web.row = self.ROW
        search_web.column = self.COLUMN
        found = search_web.get_value(user_name)
        return found

    def confirm_database_added_data(self, user_name):
        search_database = DataBase()

        result = search_database.get_employee_by_id(user_name)

        if result is not None:
            try:
                if user_name in result:
                    return True

            except Exception as e:
                print('Access Error', e)
        else:
            print('The user name does not exist')





