from pytest import mark
from utilities.libExcel import read_headers,read_valid_data, read_invalid_data
#
headers = read_headers("smoke","test_login")
valid_data = read_valid_data("smoke","test_login")
invalid_data = read_invalid_data("smoke","test_login")

@mark.parametrize(headers,valid_data)
def test_add_to_wishlist(driver,pages,email,password):
    pages.loginpage.login(email,password)
    pages.homepage.add_to_wishlist()
    assert driver.find_element("xpath","//td[text()='Product Name']/../../..//a[contains(text(),'Samsung Galaxy Tab')]").is_displayed()