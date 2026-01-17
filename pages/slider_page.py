from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from elements.input import Input
from elements.label import Label
from logger.logger import Logger


class SliderPage(BasePage):
    PATH = "/horizontal_slider"

    UNIQUE_ELEMENT_LOC = "//input[@type='range']"
    SLIDER_LOC = "//input[@type='range']"
    SLIDER_VALUE_LOC = "range"

    def __init__(self, browser):
        super().__init__(browser)

        self.page_name = "Slider Page"

        self.unique_element = Input(
            self.browser,
            self.UNIQUE_ELEMENT_LOC,
            description="Slider -> Input range"
        )

        self.slider = Input(
            self.browser,
            self.SLIDER_LOC,
            description="Slider -> Slider input"
        )

        self.slider_value = Label(
            self.browser,
            self.SLIDER_VALUE_LOC,
            description="Slider -> Value display"
        )

    def get_slider_min(self) -> float:
        """Получить минимальное значение слайдера"""
        return float(self.slider.get_attribute("min"))

    def get_slider_max(self) -> float:
        """Получить максимальное значение слайдера"""
        return float(self.slider.get_attribute("max"))

    def get_slider_step(self) -> float:
        """Получить шаг слайдера"""
        return float(self.slider.get_attribute("step"))

    def get_slider_value(self) -> float:
        """Получить текущее значение слайдера"""
        text = self.slider_value.get_text()
        return float(text)

    def set_slider_value(self, target_value: float) -> None:
        """Установить значение слайдера через Actions API"""
        Logger.info(f"{self}: set slider value to {target_value}")

        element = self.slider.wait_for_clickable()

        min_value = self.get_slider_min()
        max_value = self.get_slider_max()

        element.click()

        current_value = self.get_slider_value()
        diff = target_value - current_value
        step = self.get_slider_step()
        steps = int(diff / step)

        actions = ActionChains(self.browser.driver)
        if steps > 0:
            for _ in range(abs(steps)):
                actions.send_keys(Keys.ARROW_RIGHT)
        else:
            for _ in range(abs(steps)):
                actions.send_keys(Keys.ARROW_LEFT)
        actions.perform()
