import os
import uuid
import pytest


BROWSER_LOCATION = {
    'firefox': os.getenv('FIREFOX_BIN') or '/usr/bin/firefox',
    'chrome': os.getenv('CHROME_BIN') or '/usr/bin/google-chrome',
}


WEBDRIVER_LOCATION = {
    'firefox': os.getenv('WEBDRIVER_FIREFOX_BIN') or './bin/geckodriver',
    'chrome': os.getenv('WEBDRIVER_CHROME_BIN') or './bin/chromedriver',
}


@pytest.fixture
def selenium(selenium):
    selenium.implicitly_wait(15)
    selenium.maximize_window()
    return selenium


@pytest.fixture
def url():
    return 'https://educa.ru'

	
	
@pytest.fixture(scope='session')
def user():
    "Generate an unique email to register the user"
    return f'dmitry+{uuid.uuid4()}@gmail.com


@pytest.fixture
def driver_kwargs(request, driver_kwargs):
    """
    Generates a set of keyword arguments to WebDriver
    """
    used_driver = request.config.getoption('driver')

    if used_driver not in WEBDRIVER_LOCATION:
        pytest.fail(f'Cannot use {used_driver} coz it\'s an unknown driver')

    driver_kwargs['executable_path'] = WEBDRIVER_LOCATION[used_driver]
    return driver_kwargs


@pytest.fixture
def chrome_options(chrome_options):
    """A Silenium Chrome webdriver options.
    :type chrome_options: object
    """
    chrome_options.binary_location = BROWSER_LOCATION['chrome']
 #   chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-first-run')
    return chrome_options


@pytest.fixture
def firefox_options(firefox_options):
    """A Silenium Firefox webdriver options."""
    firefox_options.binary_location = BROWSER_LOCATION['firefox']
    chrome_options.path = "./bin/geckodriver"
    return firefox_options
