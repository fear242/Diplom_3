import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function', params=[webdriver.Firefox, webdriver.Chrome])
def driver(request):
    options = Options()
    options.add_argument('--window-size=1024,768')
    driver = request.param(options=options)
    yield driver
    driver.quit()
