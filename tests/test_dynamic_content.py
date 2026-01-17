from pages.dynamic_content_page import DynamicContentPage
from config_reader import ConfigReader

config = ConfigReader()


BASE_URL = config.base_url


class TestDynamicContent:

    def test_refresh_until_images_match(self, browser):
        """Тест #9: Обновлять страницу пока два изображения не совпадут"""
        page = DynamicContentPage(browser)
        max_attempts = 50

        browser.get(f"{BASE_URL}{page.PATH}")
        assert page.is_opened(), "Страница Dynamic Content не открылась"

        attempt = 0
        while attempt < max_attempts:
            attempt += 1

            if page.has_matching_images():
                sources = page.get_image_sources()
                assert len(set(sources)) < len(sources), \
                    f"Ожидалось совпадение изображений, Actual: {sources}"
                return

            browser.refresh_page()
            page.unique_element.wait_for_presence()

        raise AssertionError(f"Не удалось найти совпадающие изображения за {max_attempts} попыток")
