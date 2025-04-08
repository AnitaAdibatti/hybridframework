from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.common.action_chains import ActionChains
# from conftest import driver



def _wait(func):
    def wrapper(instance,locator,**kwargs):
        wait = WebDriverWait(instance.driver,10)
        v = visibility_of_element_located(locator)
        wait.until(v)
        return func(instance,locator,**kwargs)
    return wrapper

def __wait(cls):
    for key,value in cls.__dict__.items():
        if callable(value) and key != '__init__':
            setattr(cls,key,_wait(value))
    return cls

@__wait
class Selenium_wrapper:

    def __init__(self,driver):
        self.driver = driver

    def click_element(self,locator:tuple[str,str]):
        self.driver.find_element(*locator).click()

    def enter_text(self,locator,value):
        self.driver.find_element(*locator).send_keys(value)

    def select_item(self,driver, locator,item):
        element = self.driver.find_element(*locator)
        select = Select(element)
        select.select_by_visible_text(item)

    def hover_on(self,locator):
        action = ActionChains(self.driver)
        element = self.driver.find_element(*locator)
        action.move_to_element(element).perform()
