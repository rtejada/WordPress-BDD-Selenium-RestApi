from lib.pages.base_page import WordPressBasePage
from selenium.webdriver.common.by import By


class SearchByValue(WordPressBasePage):

    visible_selector = ''
    user_search_input = ''
    search_submit = ''
    table_rows_selector = ''
    row = ''
    column = ''

    def scroll_up(self):

        self.driver.execute_script("window.scrollTo(0, 10);")

    def get_value(self, search_item):

        self.wait_selector_visible(self.visible_selector)
        self.fill_text_field(self.user_search_input, search_item)
        self.send_enter_key(self.search_submit)

        rows_count = len(self.driver.find_elements(*self.table_rows_selector))

        for a in range(1, rows_count + 1):

            value = self.driver.find_element(By.XPATH, (self.row + 'tr[' + str(a) + ']' + self.column))

            if value.text == search_item:
                return True
            else:
                return False


