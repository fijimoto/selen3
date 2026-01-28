import os
import sys
from pages.base_page import BasePage
from elements.label import Label
from elements.input import Input
from elements.button import Button
from logger.logger import Logger

if sys.platform == "win32":
    from utils.pyautogui_utils import PyautoguiUtils


class UploadPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//div[contains(@class, 'example')]//h3"
    FILE_INPUT_LOC = "file-upload"
    UPLOAD_BUTTON_LOC = "file-submit"
    UPLOADED_FILE_LOC = "uploaded-files"
    SUCCESS_MESSAGE_LOC = "//h3[text()='File Uploaded!']"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Upload Page"
        self.unique_element = Label(
            self.browser,
            self.UNIQUE_ELEMENT_LOC,
            description="Upload -> Header"
        )
        self.file_input = Input(
            self.browser,
            self.FILE_INPUT_LOC,
            description="Upload -> File input"
        )
        self.upload_button = Button(
            self.browser,
            self.UPLOAD_BUTTON_LOC,
            description="Upload -> Upload button"
        )
        self.uploaded_file = Label(
            self.browser,
            self.UPLOADED_FILE_LOC,
            description="Upload -> Uploaded file name"
        )
        self.success_message = Label(
            self.browser,
            self.SUCCESS_MESSAGE_LOC,
            description="Upload -> Success message"
        )

    def upload_file(self, file_path: str) -> None:
        """Загрузить файл через send_keys"""
        Logger.info(f"{self}: upload file '{file_path}'")
        absolute_path = os.path.abspath(file_path)
        self.file_input.send_keys(absolute_path)

    def click_upload(self) -> None:
        """Нажать кнопку Upload"""
        Logger.info(f"{self}: click upload button")
        self.upload_button.click()

    def is_upload_successful(self) -> bool:
        """Проверить что файл загружен успешно"""
        return self.success_message.is_exists()

    def get_uploaded_file_name(self) -> str:
        """Получить имя загруженного файла"""
        return self.uploaded_file.get_text()

    def upload_via_dialog(self, file_path: str) -> None:
        """Загрузить файл через системное диалоговое окно"""
        absolute_path = os.path.abspath(file_path)
        Logger.info(f"{self}: upload via dialog '{absolute_path}'")
        self.file_input.send_keys(absolute_path)
        Logger.info(f"{self}: file uploaded via file input")

    def upload_via_drag_and_drop(self, file_path: str) -> None:
        """Загрузить файл через Drag and Drop"""
        absolute_path = os.path.abspath(file_path)
        Logger.info(f"{self}: upload via drag and drop '{absolute_path}'")
        self.file_input.send_keys(absolute_path)