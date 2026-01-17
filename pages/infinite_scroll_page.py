from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage
from elements.label import Label
from elements.multi_element import MultiWebElement
from logger.logger import Logger


class InfiniteScrollPage(BasePage):
    PATH = "/infinite_scroll"

    UNIQUE_ELEMENT_LOC = "//div[contains(@class, 'jscroll-inner')]"
    PARAGRAPH_LOC = "(//div[contains(@class, 'jscroll-inner')]//div[contains(@class, 'jscroll-added')])[{}]"

    def __init__(self, browser):
        super().__init__(browser)

        self.page_name = "Infinite Scroll Page"

        self.unique_element = Label(
            self.browser,
            self.UNIQUE_ELEMENT_LOC,
            description="Infinite Scroll -> Container"
        )

        self.paragraphs = MultiWebElement(
            self.browser,
            self.PARAGRAPH_LOC,
            description="Infinite Scroll -> Paragraphs"
        )

    def get_paragraphs_count(self) -> int:
        """Получить количество абзацев на странице"""
        count = sum(1 for _ in self.paragraphs)
        Logger.info(f"{self}: paragraphs count = {count}")
        return count

    def scroll_until_count(self, target_count: int, max_scrolls: int = 100) -> int:
        """Прокручивать пока не достигнем нужного количества абзацев"""
        Logger.info(f"{self}: scroll until {target_count} paragraphs")

        scrolls = 0
        paragraph_xpath = "//div[contains(@class, 'jscroll-inner')]//div[contains(@class, 'jscroll-added')]"

        while scrolls < max_scrolls:
            current_count = len(self.browser.driver.find_elements(By.XPATH, paragraph_xpath))
            if current_count >= target_count:
                Logger.info(f"{self}: reached {current_count} paragraphs")
                return current_count

            self.browser.scroll_to_bottom()

            # Ждем пока загрузятся новые элементы
            try:
                WebDriverWait(self.browser.driver, 2).until(
                    lambda driver: len(driver.find_elements(By.XPATH, paragraph_xpath)) > current_count
                )
            except:
                pass  # Если не загрузились новые элементы за 2 секунды, продолжаем

            scrolls += 1

        return len(self.browser.driver.find_elements(By.XPATH, paragraph_xpath))
