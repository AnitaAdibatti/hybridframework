# import allure
#
# from POM.loginpage import LoginPage
# from pytest import mark
# from utilities.libExcel import read_headers,read_data
#
# headers = read_headers("smoke","test_login")
# data = read_data("smoke","test_login")
#
#
# @mark.order(1)
# # @mark.dependency(name='login')
# # @mark.skip("test case working fine")
# @mark.parametrize(headers,data)
# def test_login(driver,pages,username,password):
#     pages.loginpage.login(username,password)

from selenium.webdriver.common.by import By
from pytest import mark
from utilities.libExcel import read_headers,read_valid_data, read_invalid_data
#
headers = read_headers("smoke","test_search")
valid_data = read_valid_data("smoke","test_search")
invalid_data = read_invalid_data("smoke","test_search")

@mark.parametrize(headers,valid_data)
def test_search_valid_product(driver,pages,search_key):
    # l.enter_value(("xpath","//input[@name='search']"),"HP")
    # driver.find_element("xpath","//input[@name='search']").send_keys("HP")
    # driver.find_element("xpath","//div[@id='search']//button[@type='button']").click()
    pages.homepage.search_valid_product(search_key)
    assert driver.find_element(By.LINK_TEXT,"HP LP3065").is_displayed()

@mark.parametrize(headers,invalid_data)
def test_search_invalid_product(driver,pages,search_key):
    pages.homepage.search_invalid_product(search_key)
    assert driver.find_element(By.XPATH,"//p[contains(text(),'There is no product')]").is_displayed()

