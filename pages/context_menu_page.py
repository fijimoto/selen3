from selenium.webdriver.common.action_chains import ActionChains

from pages.base_page import BasePage
from elements.label import Label
from logger.logger import Logger


class ContextMenuPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//*[contains(@id, 'hot-spot')]"
    HOT_SPOT_LOC = "//*[contains(@id, 'hot-spot')]"

    def __init__(self, browser):
        super().__init__(browser)

        self.page_name = "Context Menu Page"

        self.unique_element = Label(
            self.browser,
            self.UNIQUE_ELEMENT_LOC,
            description="Context Menu -> Hot Spot"
        )

        self.hot_spot = Label(
            self.browser,
            self.HOT_SPOT_LOC,
            description="Context Menu -> Hot Spot area"
        )

    def right_click_hot_spot(self) -> None:
        """Кликнуть правой кнопкой мыши на область"""
        Logger.info(f"{self}: right click on hot spot")
        element = self.hot_spot.wait_for_visible()
        actions = ActionChains(self.browser.driver)
        actions.context_click(element).perform()
