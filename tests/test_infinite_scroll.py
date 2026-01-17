from pages.infinite_scroll_page import InfiniteScrollPage
from config_reader import ConfigReader

config = ConfigReader()


BASE_URL = config.base_url


class TestInfiniteScroll:

    def test_scroll_to_age(self, browser):
        """Тест #10: Прокрутить страницу"""
        page = InfiniteScrollPage(browser)
        my_age = 24

        browser.get(f"{BASE_URL}{page.PATH}")
        assert page.is_opened(), "Страница Infinite Scroll не открылась"

        actual_count = page.scroll_until_count(my_age)

        assert actual_count >= my_age, \
            f"Expected at least {my_age} paragraphs, Actual: {actual_count}"
