from time import sleep

from pytest import mark
from utilities.libExcel import read_headers,read_valid_data, read_invalid_data
#
headers = read_headers("smoke","test_login")
valid_data = read_valid_data("smoke","test_login")
invalid_data = read_invalid_data("smoke","test_login")


# @mark.order(1)
# @mark.skip("test case working fine")
@mark.parametrize(headers,valid_data)
def test_login_with_valid_data(driver,pages,email,password):
    pages.loginpage.login(email,password)
    assert driver.find_element("xpath","//div[@id='content']//h2[.='My Account']").is_displayed()

@mark.parametrize(headers,invalid_data)
def test_login_with_invalid_data(driver,pages,email,password):
    pages.loginpage.login(email,password)
    sleep(2)
    assert driver.find_element("xpath","//div[contains(text(),'Warning:')]").is_displayed()