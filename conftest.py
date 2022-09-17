import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

path_to_driver = r"/Users/e.kazimirova/Downloads/"
path_to_binary_location_yandex = '/Applications/Yandex.app/Contents/MacOS/Yandex'
# path_to_binary_location_opera = '/Applications/Opera.app/Contents/MacOS/Opera' The Opera driver no longer works
# with the latest functionality of Selenium and is currently officially unsupported.


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="http://192.168.0.5:8081/",
        help="This is request url"
    )

    parser.addoption(
        "--browser",
        default="chrome",
        help="This is the browser we use"
    )


@pytest.fixture
def open_browser(request):
    browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--url")

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=options)
    # elif browser == "opera":
    #     options = webdriver.ChromeOptions()
    #     options.binary_location = path_to_binary_location_opera
    #     driver = webdriver.Chrome(options=options)
    elif browser == "yandex":
        options = webdriver.ChromeOptions()
        service = Service(executable_path=path_to_driver + "yandexdriver")
        options.binary_location = path_to_binary_location_yandex
        driver = webdriver.Chrome(service=service, options=options)
    elif browser == "firefox":
        service = FirefoxService(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
    elif browser == "safari":
        driver = webdriver.Safari()
    else:
        raise Exception("Driver not found!")

    driver.base_url = base_url

    yield driver

    driver.close()
