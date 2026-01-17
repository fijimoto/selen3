from pages.base_page import BasePage
from elements.label import Label


class NewWindowPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//h3[text()='New Window']"
    HEADER_LOC = "//h3"

    def __init__(self, browser):
        super().__init__(browser)

        self.page_name = "New Window Page"

        self.unique_element = Label(
            self.browser,
            self.UNIQUE_ELEMENT_LOC,
            description="New Window -> Header"
        )

        self.header = Label(
            self.browser,
            self.HEADER_LOC,
            description="New Window -> Header text"
        )

    def get_header_text(self) -> str:
        """Получить текст заголовка"""
        return self.header.get_text()
