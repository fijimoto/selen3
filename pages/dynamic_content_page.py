from pages.base_page import BasePage
from elements.label import Label
from elements.multi_element import MultiWebElement
from logger.logger import Logger


class DynamicContentPage(BasePage):
    UNIQUE_ELEMENT_LOC = "content"
    IMAGE_LOC = "(//*[@id='content']//*[contains(@class, 'large-2') and contains(@class, 'columns')]//img)[{}]"

    def __init__(self, browser):
        super().__init__(browser)

        self.page_name = "Dynamic Content Page"

        self.unique_element = Label(
            self.browser,
            self.UNIQUE_ELEMENT_LOC,
            description="Dynamic Content -> Header"
        )

        self.images = MultiWebElement(
            self.browser,
            self.IMAGE_LOC,
            description="Dynamic Content -> Images"
        )

    def get_image_sources(self) -> list[str]:
        """Получить список src всех изображений"""
        Logger.info(f"{self}: get image sources")
        sources = [image.get_attribute("src") for image in self.images]
        Logger.info(f"{self}: found {len(sources)} images")
        return sources

    def has_matching_images(self) -> bool:
        """Проверить есть ли два одинаковых изображения"""
        sources = self.get_image_sources()
        unique_sources = set(sources)
        has_match = len(unique_sources) < len(sources)
        Logger.info(f"{self}: has matching images = {has_match}")
        return has_match
