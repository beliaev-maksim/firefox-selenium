import pytest
from selenium import webdriver

from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service


@pytest.fixture(scope='session')
def driver(request):
    """Set up webdriver fixture."""
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    service = Service(executable_path="firefox.geckodriver")
    driver = webdriver.Firefox(options=options, service=service)
    driver.set_window_size(1920, 1080)
    driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver
    driver.quit()
