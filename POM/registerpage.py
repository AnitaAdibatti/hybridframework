from utilities.lib import Selenium_wrapper
from utilities.libExcel import read_locator

@read_locator('registerpage')
class RegisterPage:

    def __init__(self,driver):
        self.driver = driver
        self.wrapper = Selenium_wrapper(self.driver)

    def register(self,first_name,last_name,email,telephone,password,confirmpass):
        self.wrapper.click_element(self.myaccount_link)
        self.wrapper.click_element(self.register_link)
        self.wrapper.enter_text(self.firstname,value=first_name)
        self.wrapper.enter_text(self.lastname,value=last_name)
        self.wrapper.enter_text(self.email,value=email)
        self.wrapper.enter_text(self.telephone,value=telephone)
        self.wrapper.enter_text(self.password,value=password)
        self.wrapper.enter_text(self.confirmpass,value=confirmpass)
        self.wrapper.click_element(self.checkbox)
        self.wrapper.click_element(self.submit_button)
