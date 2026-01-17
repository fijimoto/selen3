from pages.base_page import BasePage
from elements.label import Label
from logger.logger import Logger


class NestedFramesPage(BasePage):
    UNIQUE_ELEMENT_LOC = "framesWrapper"
    PARENT_FRAME_LOC = "frame1"
    CHILD_FRAME_LOC = "//iframe[@srcdoc]"
    PARENT_FRAME_TEXT_LOC = "//body"
    CHILD_FRAME_TEXT_LOC = "//p"

    def __init__(self, browser):
        super().__init__(browser)

        self.page_name = "Nested Frames Page"

        self.unique_element = Label(
            self.browser,
            self.UNIQUE_ELEMENT_LOC,
            description="Nested Frames -> Wrapper"
        )

        self.parent_frame = Label(
            self.browser,
            self.PARENT_FRAME_LOC,
            description="Nested Frames -> Parent frame"
        )

        self.child_frame = Label(
            self.browser,
            self.CHILD_FRAME_LOC,
            description="Nested Frames -> Child frame"
        )

        self.parent_frame_text = Label(
            self.browser,
            self.PARENT_FRAME_TEXT_LOC,
            description="Nested Frames -> Parent frame text"
        )

        self.child_frame_text = Label(
            self.browser,
            self.CHILD_FRAME_TEXT_LOC,
            description="Nested Frames -> Child frame text"
        )

    def get_parent_frame_text(self) -> str:
        """Получить текст из parent frame (транзакционно - возвращает контекст)"""
        Logger.info(f"{self}: get parent frame text")
        self.browser.switch_to_frame(self.parent_frame)
        text = self.parent_frame_text.get_text()
        return text

    def get_child_frame_text(self) -> str:
        """Получить текст из child frame (уже внутри parent, возвращает контекст)"""
        Logger.info(f"{self}: get child frame text")
        self.browser.switch_to_frame(self.child_frame)
        text = self.child_frame_text.get_text()
        self.browser.switch_to_default_content()
        return text
