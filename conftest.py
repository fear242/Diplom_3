import pytest
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from faker import Faker
import requests
import data

fake = Faker(['ru_RU'])


@pytest.fixture(scope='function', params=['Chrome', 'Firefox'])
def driver(request):
    if request.param == 'Chrome':
        chromedriver_autoinstaller.install()
        options = ChromeOptions()
        options.add_argument('--window-size=1280,768')
        driver = webdriver.Chrome(options=options)
    elif request.param == 'Firefox':
        options = FirefoxOptions()
        options.add_argument("--width=1280")
        options.add_argument("--height=768")
        driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()


@pytest.fixture()
def registered_user():
    email = fake.email()
    password = fake.password()
    name = fake.name()

    payload = {
        "email": email,
        "password": password,
        "name": name
    }
    response = requests.post(data.URL_register, data=payload)
    yield payload
    requests.delete(data.URL_user, headers={'authorization': response.json()["accessToken"]})
