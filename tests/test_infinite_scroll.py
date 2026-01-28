from pages.infinite_scroll_page import InfiniteScrollPage
from config_reader import ConfigReader

config = ConfigReader()


BASE_URL = config.base_url


class TestInfiniteScroll:

    def test_scroll_to_age(self, browser):
        """Тест #10: Прокрутить страницу"""
        page = InfiniteScrollPage(browser)
        my_age = 24

        browser.get(f"{BASE_URL}/infinite_scroll")
        assert page.is_opened(), "Страница Infinite Scroll не открылась"

        paragraphs = page.scroll_element(my_age)

        assert len(paragraphs) >= my_age, \
            f"Expected at least {my_age} paragraphs, Actual: {len(paragraphs)}"
