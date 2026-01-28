from pages.base_page import BasePage
from elements.button import Button
from elements.label import Label
from logger.logger import Logger


class FramesPage(BasePage):
    DEMOQA_URL = "https://demoqa.com/frames"

    UNIQUE_ELEMENT_LOC = "//div[contains(@class, 'example')]//h3"
    ALERTS_MENU_LOC = "//span[text()='Alerts, Frame & Windows']"
    NESTED_FRAMES_MENU_LOC = "//span[text()='Nested Frames']"
    FRAMES_MENU_LOC = "//*[@id='item-2']//span[text()='Frames']"

    def __init__(self, browser):
        super().__init__(browser)

        self.page_name = "Frames Page"

        self.unique_element = Label(
            self.browser,
            self.UNIQUE_ELEMENT_LOC,
            description="Frames -> Header"
        )

        self.alerts_menu = Button(
            self.browser,
            self.ALERTS_MENU_LOC,
            description="Frames -> Alerts menu"
        )

        self.nested_frames_menu = Button(
            self.browser,
            self.NESTED_FRAMES_MENU_LOC,
            description="Frames -> Nested Frames menu"
        )

        self.frames_menu = Button(
            self.browser,
            self.FRAMES_MENU_LOC,
            description="Frames -> Frames menu"
        )

    def click_alerts_menu(self) -> None:
        """Кликнуть на меню Alerts, Frame & Windows"""
        Logger.info(f"{self}: click Alerts menu")
        self.alerts_menu.click()

    def click_nested_frames_menu(self) -> None:
        """Кликнуть на меню Nested Frames через JS"""
        Logger.info(f"{self}: click Nested Frames menu")
        self.nested_frames_menu.js_click()

    def click_frames_menu(self) -> None:
        """Кликнуть на меню Frames"""
        Logger.info(f"{self}: click Frames menu")
        self.frames_menu.click()
