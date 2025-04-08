from time import sleep

from pytest import mark
from utilities.libExcel import read_headers,read_valid_data, read_invalid_data
#
headers = read_headers("smoke","test_register")
valid_data = read_valid_data("smoke","test_register")
invalid_data = read_invalid_data("smoke","test_register")

# @mark.dependency(name='test_login')
@mark.skip
@mark.parametrize(headers,valid_data)
def test_register_with_valid_data(driver,pages,first_name,last_name,email,telephone,password,confirmpass):
    pages.registerpage.register(first_name,last_name,email,telephone,password,confirmpass)
    # assert driver.find_element("xpath","//div[contains(text(),'Warning')]").is_displayed()
    register_message = driver.find_element("xpath","//div[@id='content']//h1")
    success_text = register_message.text
    assert success_text=="Your Account Has Been Created!"

@mark.parametrize(headers,invalid_data)
def test_register_with_invalid_data(driver,pages,first_name,last_name,email,telephone,password,confirmpass):
    pages.registerpage.register(first_name, last_name, email, telephone, password, confirmpass)
    sleep(3)
    assert driver.find_element("xpath","//div[contains(text(),'Warning')]").is_displayed()