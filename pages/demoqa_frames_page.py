from pages.base_page import BasePage
from elements.label import Label
from logger.logger import Logger


class DemoqaFramesPage(BasePage):
    UNIQUE_ELEMENT_LOC = "framesWrapper"
    FRAME_TOP_LOC = "frame1"
    FRAME_BOTTOM_LOC = "frame2"
    FRAME_HEADING_LOC = "sampleHeading"

    def __init__(self, browser):
        super().__init__(browser)

        self.page_name = "Demoqa Frames Page"

        self.unique_element = Label(
            self.browser,
            self.UNIQUE_ELEMENT_LOC,
            description="Demoqa Frames -> Wrapper"
        )

        self.frame_top = Label(
            self.browser,
            self.FRAME_TOP_LOC,
            description="Demoqa Frames -> Top frame"
        )

        self.frame_bottom = Label(
            self.browser,
            self.FRAME_BOTTOM_LOC,
            description="Demoqa Frames -> Bottom frame"
        )

        self.frame_heading = Label(
            self.browser,
            self.FRAME_HEADING_LOC,
            description="Demoqa Frames -> Frame heading"
        )

    def get_top_frame_text(self) -> str:
        """Получить текст из верхнего фрейма"""
        Logger.info(f"{self}: get top frame text")
        self.browser.switch_to_frame(self.frame_top)
        text = self.frame_heading.get_text()
        self.browser.switch_to_default_content()
        return text

    def get_bottom_frame_text(self) -> str:
        """Получить текст из нижнего фрейма"""
        Logger.info(f"{self}: get bottom frame text")
        self.browser.switch_to_frame(self.frame_bottom)
        text = self.frame_heading.get_text()
        self.browser.switch_to_default_content()
        return text
