from elements.label import Label
from elements.button import Button
from pages.base_page import BasePage


class WindowsPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//div[contains(@class, 'example')]//h3"
    CLICK_HERE_LINK_LOC = "//a[contains(text(), 'Click Here')]"

    def __init__(self, browser):
        super().__init__(browser)

        self.page_name = "Windows Page"

        self.unique_element = Label(
            self.browser,
            self.UNIQUE_ELEMENT_LOC,
            description="Windows -> Header"
        )

        self.click_here_link = Button(
            self.browser,
            self.CLICK_HERE_LINK_LOC,
            description="Windows -> Click Here link"
        )

    def click_link(self) -> None:
        """Кликнуть на ссылку Click Here"""
        self.click_here_link.click()
