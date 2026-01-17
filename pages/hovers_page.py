from selenium.webdriver.common.action_chains import ActionChains

from pages.base_page import BasePage
from elements.button import Button
from elements.label import Label
from elements.multi_element import MultiWebElement
from logger.logger import Logger


class HoversPage(BasePage):
    PATH = "/hovers"

    UNIQUE_ELEMENT_LOC = "//div[contains(@class, 'example')]"
    USER_CARD_LOC = "(//div[contains(@class, 'figure')])[{}]"

    USER_CARD_BY_INDEX_TPL = "(//div[contains(@class, 'figure')])[{index}]"
    USER_NAME_BY_INDEX_TPL = "(//div[contains(@class, 'figure')])[{index}]//h5"
    USER_PROFILE_BY_INDEX_TPL = "(//div[contains(@class, 'figure')])[{index}]//a[contains(text(), 'View profile')]"

    def __init__(self, browser):
        super().__init__(browser)

        self.page_name = "Hovers Page"

        self.unique_element = Label(
            self.browser,
            self.UNIQUE_ELEMENT_LOC,
            description="Hovers -> Example container"
        )

        self.user_cards = MultiWebElement(
            self.browser,
            self.USER_CARD_LOC,
            description="Hovers -> User cards"
        )

    def get_user_cards_count(self) -> int:
        """Получить количество карточек пользователей"""
        return sum(1 for _ in self.user_cards)

    def hover_user(self, index: int) -> None:
        """Навести курсор на пользователя по индексу (1-based)"""
        Logger.info(f"{self}: hover user #{index}")
        locator = self.USER_CARD_BY_INDEX_TPL.format(index=index)
        element = Label(
            self.browser,
            locator,
            description=f"Hovers -> User card #{index}"
        )
        card = element.wait_for_visible()
        actions = ActionChains(self.browser.driver)
        actions.move_to_element(card).perform()

    def get_user_name(self, index: int) -> str:
        """Получить имя пользователя после hover"""
        Logger.info(f"{self}: get user name #{index}")
        locator = self.USER_NAME_BY_INDEX_TPL.format(index=index)
        element = Label(
            self.browser,
            locator,
            description=f"Hovers -> User #{index} name"
        )
        return element.get_text()

    def click_user_profile(self, index: int) -> None:
        """Кликнуть на ссылку профиля пользователя"""
        Logger.info(f"{self}: click user profile #{index}")
        locator = self.USER_PROFILE_BY_INDEX_TPL.format(index=index)
        link = Button(
            self.browser,
            locator,
            description=f"Hovers -> User #{index} profile link"
        )
        link.click()
