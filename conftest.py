import pytest
from selenium import webdriver



def pytest_addoption(parser):
    parser.addoption('--language', default='en')


@pytest.fixture
def config(request):
    language=request.config.getoption('--language')
    return {'language':language}

@pytest.fixture
def driver(config):
    lan=config['language']
    url = f'http://selenium1py.pythonanywhere.com/{lan}'
    browser=webdriver.Chrome()
    browser.get(url)
    yield browser
    browser.quit()
