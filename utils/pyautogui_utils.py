import time
import pyautogui
import pyperclip

from logger.logger import Logger


class PyautoguiUtils:
    @staticmethod
    def upload_file(file_path: str) -> None:
        """Загрузить файл через диалоговое окно Windows (только горячие клавиши)"""
        Logger.info("Handle File Dialog for uploading file")

        pyperclip.copy(file_path)
        Logger.info(f"Path copied to clipboard: {file_path}")

        time.sleep(1)

        pyautogui.hotkey('ctrl', 'v')
        Logger.info("Pasted path from clipboard")

        time.sleep(0.5)

        pyautogui.press('enter')
        Logger.info("Pressed Enter")

        time.sleep(2)
