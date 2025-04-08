from utilities.lib import Selenium_wrapper
from utilities.libExcel import read_locator

@read_locator('loginpage')
class LoginPage:

    def __init__(self,driver):
        self.driver = driver
        self.wrapper = Selenium_wrapper(self.driver)

    def login(self,email,password):
        self.wrapper.click_element(self.myaccount_link)
        self.wrapper.click_element(self.login_link)
        self.wrapper.enter_text(self.email_textbox,value=email)
        self.wrapper.enter_text(self.password_textbox,value=password)
        self.wrapper.click_element(self.login_button)

    def login_with_valid_data(self,email,password):
        self.wrapper.click_element(self.myaccount_link)
        self.wrapper.click_element(self.login_link)
        self.wrapper.enter_text(self.email_textbox, value=email)
        self.wrapper.enter_text(self.password_textbox, value=password)
        self.wrapper.click_element(self.login_button)