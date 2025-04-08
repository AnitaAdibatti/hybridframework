# from conftest import driver
from time import sleep

from utilities.lib import Selenium_wrapper
from utilities.libExcel import read_locator

@read_locator('homepage')
class HomePage:

    def __init__(self,driver):
        self.driver = driver
        self.wrapper = Selenium_wrapper(self.driver)

    def search_valid_product(self,search_key):
        self.wrapper.enter_text(self.search_box,value=search_key)
        self.wrapper.click_element(self.search_button)

    def search_invalid_product(self,search_key):
        self.wrapper.enter_text(self.search_box,value=search_key)
        self.wrapper.click_element(self.search_button)

    def add_to_wishlist(self):
        self.wrapper.click_element(self.tablets_link)
        self.wrapper.click_element(self.samsung_tablet_wishlist_button)
        self.wrapper.click_element(self.wishlist_link)

    def add_to_cart(self):
        self.wrapper.hover_on(self.desktops_link)
        self.wrapper.click_element(self.mac_link)
        self.wrapper.click_element(self.addtocart_imac_buttton)
        sleep(2)
        assert self.driver.find_element(*(self.success_msg_addedtocart)).is_displayed()
        self.wrapper.click_element(self.shoppingcart_link)
        sleep(2)
        assert self.driver.find_element(*(self.iMac_productname)).is_displayed()