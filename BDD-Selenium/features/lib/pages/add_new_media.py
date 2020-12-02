from selenium.webdriver.common.by import By
from lib.pages.base_page import WordPressBasePage
import os


class NewMedia(WordPressBasePage):
    MENU_MEDIA = (By.ID, 'menu-media')
    NEW_MEDIA = (By.LINK_TEXT, 'Añadir nuevo')
    WPBODY = (By.ID, 'wpbody')
    UPLOAD = (By.ID, 'plupload-browse-button')
    HTML_UPLOAD = (By.ID, 'html-upload')
    PATH = os.getcwd() + "/BDD-Selenium/features/lib/data/images/"

    def access_media(self):
        self.click_button(self.MENU_MEDIA)
        self.click_button(self.NEW_MEDIA)

    def add_new_media(self):
        self.wait_selector_visible(self.WPBODY)
        self.wait_button_clickable(self.UPLOAD)
        self.driver.find_element(*self.UPLOAD).send_keys(self.PATH+'apu.jpg')


