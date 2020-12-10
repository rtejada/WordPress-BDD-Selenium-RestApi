from lib.pages.base_page import WordPressBasePage
from selenium.webdriver.common.by import By


class SearchDataElements(WordPressBasePage):

    visible_selector = ''
    all_entries = ''
    visible_search = ''
    user_search_input = ''
    search_submit = ''
    table_rows_selector = ''
    row = ''
    column = ''

    def get_element(self, search_item):

        self.wait_selector_visible(self.visible_selector)
        self.click_button(self.all_entries)
        self.wait_selector_visible(self.visible_search)
        self.fill_text_field(self.user_search_input, search_item)
        self.send_enter_key(self.search_submit)

        rows_count = len(self.driver.find_elements(*self.table_rows_selector))

        for a in range(1, rows_count + 1):

            value = self.driver.find_element(By.XPATH, (self.row + 'tr[' + str(a) + ']' + self.column))

            if value.text == search_item.lower():
                return True
            else:
                return False
