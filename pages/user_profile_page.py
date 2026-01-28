from pages.base_page import BasePage
from elements.label import Label


class UserProfilePage(BasePage):
    UNIQUE_ELEMENT_LOC = "//h1"
    HEADER_LOC = "//h1"

    def __init__(self, browser):
        super().__init__(browser)

        self.page_name = "User Profile Page"

        self.unique_element = Label(
            self.browser,
            self.UNIQUE_ELEMENT_LOC,
            description="User Profile -> Header"
        )

        self.header = Label(
            self.browser,
            self.HEADER_LOC,
            description="User Profile -> Header text"
        )

    def get_header_text(self) -> str:
        """Получить текст заголовка"""
        return self.header.get_text()
