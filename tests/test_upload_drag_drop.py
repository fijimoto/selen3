import os

from pages.upload_page import UploadPage
from config_reader import ConfigReader

config = ConfigReader()


BASE_URL = config.base_url


class TestUploadDragDrop:

    def test_upload_drag_and_drop(self, browser):
        """Тест #13: Загрузить файл через Drag and Drop зону"""
        page = UploadPage(browser)
        test_file_path = os.path.join(os.path.dirname(
            __file__), "..", "resources", "test_file.txt")
        test_file_path = os.path.abspath(test_file_path)

        browser.get(f"{BASE_URL}/upload")
        assert page.is_opened(), "Страница Upload не открылась"

        page.upload_via_drag_and_drop(test_file_path)

        page.click_upload()

        assert page.is_upload_successful(), "Сообщение 'File Uploaded!' не появилось"
