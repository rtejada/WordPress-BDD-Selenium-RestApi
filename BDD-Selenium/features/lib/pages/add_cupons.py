from lib.pages.base_page import WordPressBasePage
from lib.pages.sub_pages.search_data_elements import SearchDataElements
from selenium.webdriver.common.by import By


class Coupons(WordPressBasePage):

    MARKETING = (By.LINK_TEXT, 'Marketing')
    COUPONS = (By.LINK_TEXT, 'Cupones')
    WPBODY = (By.ID, 'wpbody')
    ADD_COUPON = (By.LINK_TEXT, 'Añadir cupón')
    TITLE = (By.ID, 'title')
    COUPON_DESCRIPTION = (By.ID, 'woocommerce-coupon-description')
    TAXONOMY_PRODUCT = (By.ID, 'taxonomy-product_cat')
    DISCOUNT_TYPE = (By.ID, 'discount_type')
    VALUE = "fixed_cart"
    COUPON_AMOUNT = (By.ID, 'coupon_amount')
    FREE_SHIPPING = (By.ID, 'free_shipping')
    EXPIRE_DATE = (By.ID, 'expiry_date')
    CALENDAR = (By.ID, 'ui-datepicker-div')
    DATE = (By.XPATH, '//*[@id="ui-datepicker-div"]/table/tbody/tr[4]/td[2]/a')
    PUBLISH = (By.ID, 'publish')
    ALL_PAGES = (By.LINK_TEXT, 'Todos los productos')
    POST_SEARCH_INPUT = (By.ID, 'post-search-input')
    SEARCH_SUBMIT = (By.ID, 'search-submit')
    TABLE_ROWS_SELECTOR = (By.XPATH, '//*[@id="the-list"]/tr')
    ROW = '//*[@id="the-list"]/'
    COLUMN = '/td[1]/strong/a'

    def access_marketing(self):
        self.click_button(self.MARKETING)
        self.click_button(self.COUPONS)

    def add_new_coupon(self):

        title_coupon = self.random_letter(12)
        self.wait_selector_visible(self.WPBODY)
        self.click_button(self.ADD_COUPON)
        self.wait_selector_visible(self.WPBODY)
        self.fill_text_field(self.TITLE, title_coupon)
        self.fill_text_field(self.COUPON_DESCRIPTION, self.random_letter(25))
        self.fill_select_by_value(self.DISCOUNT_TYPE, self.VALUE)
        self.fill_text_field(self.COUPON_AMOUNT, '100')
        self.click_button(self.FREE_SHIPPING)
        self.click_button(self.EXPIRE_DATE)
        self.wait_selector_visible(self.CALENDAR)
        self.click_button(self.DATE)
        self.send_enter_key(self.PUBLISH)

        return title_coupon

    def confirm_data_coupons(self, coupon):
        coupon = coupon.lower()
        search_web = SearchDataElements(self.driver)
        search_web.visible_selector = self.COUPONS
        search_web.all_entries = self.COUPONS
        search_web.visible_search = self.WPBODY
        search_web.user_search_input = self.POST_SEARCH_INPUT
        search_web.search_submit = self.SEARCH_SUBMIT
        search_web.table_rows_selector = self.TABLE_ROWS_SELECTOR
        search_web.row = self.ROW
        search_web.column = self.COLUMN
        found = search_web.get_element(coupon)
        return found



