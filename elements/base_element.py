from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from logger.logger import Logger


class BaseElement:
    TIMEOUT = 10

    def __init__(self, browser, locator: str, description: str = ""):
        self.browser = browser
        self.locator = self._parse_locator(locator)
        self.description = description

        self._wait = WebDriverWait(browser.driver, self.TIMEOUT)

    def _parse_locator(self, locator: str) -> tuple:
        """Определить тип локатора: ID или XPATH"""
        if locator.startswith("//") or locator.startswith("(//"):
            return (By.XPATH, locator)
        return (By.ID, locator)

    def wait_for_presence(self):
        """Ждать появления элемента в DOM"""
        Logger.info(f"{self}: wait for presence")
        return self._wait.until(EC.presence_of_element_located(self.locator))

    def wait_for_visible(self):
        """Ждать видимости элемента"""
        Logger.info(f"{self}: wait for visible")
        return self._wait.until(EC.visibility_of_element_located(self.locator))

    def wait_for_clickable(self):
        """Ждать кликабельности элемента"""
        Logger.info(f"{self}: wait for clickable")
        return self._wait.until(EC.element_to_be_clickable(self.locator))

    def click(self) -> None:
        """Кликнуть на элемент"""
        Logger.info(f"{self}: click")
        self.wait_for_clickable().click()

    def js_click(self) -> None:
        """Кликнуть через JavaScript (для перекрытых элементов)"""
        Logger.info(f"{self}: js click")
        element = self.wait_for_presence()
        self.browser.execute_script("arguments[0].click();", element)

    def get_text(self) -> str:
        """Получить текст элемента"""
        Logger.info(f"{self}: get text")
        element = self.wait_for_presence()
        text = element.text
        Logger.info(f"{self}: text = '{text}'")
        return text

    def get_attribute(self, name: str) -> str:
        """Получить атрибут элемента"""
        Logger.info(f"{self}: get attribute '{name}'")
        return self.wait_for_presence().get_attribute(name)

    def is_enabled(self) -> bool:
        """Проверить что элемент активен"""
        element = self.wait_for_presence()
        Logger.info(f"{self}: is enabled")
        result = element.is_enabled()
        Logger.info(f"{self}: is enabled = {result}")
        return result

    def is_displayed(self) -> bool:
        """Проверить что элемент видим"""
        Logger.info(f"{self}: is displayed")
        return self.wait_for_presence().is_displayed()

    def is_exists(self) -> bool:
        """Проверить существование элемента"""
        Logger.info(f"{self}: is exists")
        try:
            self._wait.until(EC.presence_of_element_located(self.locator))
            return True
        except TimeoutException:
            return False

    def __str__(self) -> str:
        return f"{self.__class__.__name__}[{self.description}]"

    def __repr__(self) -> str:
        return str(self)
