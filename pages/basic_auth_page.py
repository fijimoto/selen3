from pages.base_page import BasePage
from elements.label import Label


class BasicAuthPage(BasePage):
    UNIQUE_ELEMENT_LOC = "content"
    CONTENT_LOC = "//*[@id='content']//p"

    def __init__(self, browser):
        super().__init__(browser)

        self.page_name = "Basic Auth Page"

        self.unique_element = Label(
            self.browser,
            self.UNIQUE_ELEMENT_LOC,
            description="Basic Auth -> Content div"
        )

        self.content = Label(
            self.browser,
            self.CONTENT_LOC,
            description="Basic Auth -> Content text"
        )

    def get_content_text(self) -> str:
        """Получить текст контента страницы"""
        return self.content.get_text()
