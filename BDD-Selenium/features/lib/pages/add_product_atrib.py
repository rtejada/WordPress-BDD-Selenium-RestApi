from selenium.webdriver.common.by import By
from lib.pages.base_page import WordPressBasePage
from lib.pages.sub_pages.finding_results import SearchByValue


class NewProductAttribute(WordPressBasePage):
    MENU_PAGES = (By.ID, 'menu-posts-product')
    NEW_ATTRIBUTE = (By.LINK_TEXT, 'Atributos')
    WPBODY = (By.ID, 'wpbody')
    ATTRIB_NAME = (By.ID, 'attribute_label')
    ATTRIB_SLUG = (By.ID, 'attribute_name')
    ATTRIBUTE_PUBLIC = (By.ID, 'attribute_public')
    ATTRIBUTE_ORDERBY = (By.ID, 'attribute_orderby')
    SUBMIT = (By.ID, 'submit')
    BODY_CONTENT = (By.ID, 'col-right')
    TABLE_ROWS_SELECTOR = (By.XPATH, '//tbody/tr')
    ROW = '//tbody/'
    COLUMN = '/td[1]/strong/a'

    def access_attrib(self):
        self.click_button(self.MENU_PAGES)
        self.click_button(self.NEW_ATTRIBUTE)

    def add_attrib(self):

        attrib_name = 'Attrib-'+self.random_letter(7)

        self.wait_selector_visible(self.WPBODY)
        self.fill_text_field(self.ATTRIB_NAME, attrib_name)
        self.fill_text_field(self.ATTRIB_SLUG, self.random_letter(7))
        self.click_button(self.ATTRIBUTE_PUBLIC)
        self.fill_select_by_text(self.ATTRIBUTE_ORDERBY, 'Nombre')
        self.send_enter_key(self.SUBMIT)

        return attrib_name

    def confirm_data_attrib(self, attrib_name):

        self.wait_selector_visible(self.BODY_CONTENT)
        rows_count = len(self.driver.find_elements(*self.TABLE_ROWS_SELECTOR))

        for a in range(1, rows_count + 1):

            value = self.driver.find_element(By.XPATH, (self.ROW + 'tr[' + str(a) + ']' + self.COLUMN))

            return value.text == attrib_name
