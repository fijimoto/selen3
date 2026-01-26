import os
import pytest
from browser.browser import Browser
from browser.browser_factory import BrowserFactory
from config_reader import ConfigReader

config = ConfigReader()


@pytest.fixture(scope="function")
def browser():
    options = []

    if os.getenv("DOCKER_ENV"):
        options = [
            "--headless",
            "--no-sandbox",
            "--disable-dev-shm-usage"
        ]

    driver = BrowserFactory.get_driver(
        window_size=config.pc_window_size,
        options=options
    )
    browser = Browser(driver)
    yield browser
    browser.quit()