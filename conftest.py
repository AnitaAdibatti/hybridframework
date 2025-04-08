from pytest import fixture
from selenium.webdriver.chrome.webdriver import WebDriver as Chrome
from selenium.webdriver.firefox.webdriver import WebDriver as Firefox
from selenium.webdriver.edge.webdriver import WebDriver as Edge
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from POM.homepage import HomePage
from POM.loginpage import LoginPage
from POM.registerpage import RegisterPage


def pytest_addoption(parser):
    parser.addoption("--browser", action='store', default='chrome', dest='browser')
    parser.addoption("--env", action='store', default='Test', dest='env')
    parser.addoption("--headless", action='store_true', dest='headless', default=False)


@fixture
def _config(request):
    class TestConfigurations:
        url = "https://tutorialsninja.com/demo/"
        username = ''
        password = ''

    class StageConfigurations:
        url = "https://tutorialsninja.com/demo/"

    exe_env = request.config.option.env

    if exe_env.upper() == "TEST":
        print("Execution environment is TEST")
        return TestConfigurations()
    elif exe_env.upper() == "STAGE":
        print("Execution environment is STAGE")
        return StageConfigurations()
    else:
        raise Exception("Invalid execution environment")


@fixture
def driver(request,_config):
    browser_name = request.config.option.browser
    is_headless = request.config.option.headless
    options = None

    print("executing setup")
    if browser_name.upper() == "CHROME":
        if is_headless:
            options = ChromeOptions()
            options.add_argument("--headless=new")
        _driver = Chrome(options=options)
    elif browser_name.upper() == "FIREFOX":
        if is_headless:
            options = FirefoxOptions()
            options.add_argument("--headless")
        _driver = Firefox(options=options)
    elif browser_name.upper() == "EDGE":
        if is_headless:
            options = EdgeOptions()
            options.add_argument("--headless=new")
        _driver = Edge(options=options)
    else:
        raise Exception("Invalid browser")
    _driver.get(_config.url)
    _driver.maximize_window()
    yield _driver
    print("executing tear down")
    _driver.quit()

@fixture
def pages(driver):
    class Pages:
        homepage = HomePage(driver)
        loginpage = LoginPage(driver)
        registerpage = RegisterPage(driver)
    return Pages()