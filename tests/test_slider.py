import random

from pages.slider_page import SliderPage
from config_reader import ConfigReader

config = ConfigReader()


BASE_URL = config.base_url


class TestSlider:

    def test_horizontal_slider(self, browser):
        """Тест #5: Установить случайное значение слайдера и проверить"""
        page = SliderPage(browser)

        browser.get(f"{BASE_URL}{page.PATH}")
        assert page.is_opened(), "Страница Slider не открылась"

        min_value = page.get_slider_min()
        max_value = page.get_slider_max()
        step = page.get_slider_step()

        steps_count = int((max_value - min_value) / step)
        random_steps = random.randint(1, steps_count - 1)
        target_value = min_value + (random_steps * step)

        page.set_slider_value(target_value)

        actual_value = page.get_slider_value()
        assert actual_value == target_value, \
            f"Expected: {target_value}, Actual: {actual_value}"
