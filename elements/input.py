from elements.base_element import BaseElement
from logger.logger import Logger


class Input(BaseElement):

    def send_keys(self, text: str) -> None:
        """Отправить текст в элемент"""
        Logger.info(f"{self}: send keys '{text}'")
        self.wait_for_visible().send_keys(text)

    def clear(self) -> None:
        """Очистить поле ввода"""
        Logger.info(f"{self}: clear")
        self.wait_for_visible().clear()

    def clear_and_send_keys(self, text: str) -> None:
        """Очистить и ввести текст"""
        self.clear()
        self.send_keys(text)
