import os

from pages.upload_page import UploadPage
from config_reader import ConfigReader

config = ConfigReader()


BASE_URL = config.base_url


class TestUploadDialog:

    def test_upload_via_dialog(self, browser):
        """Тест #12: Загрузить файл через диалоговое окно"""
        page = UploadPage(browser)
        test_file_path = os.path.join(os.path.dirname(
            __file__), "..", "resources", "test_image.png")
        test_file_path = os.path.abspath(test_file_path)

        browser.get(f"{BASE_URL}/upload")
        assert page.is_opened(), "Страница Upload не открылась"

        page.upload_via_dialog(test_file_path)

        file_input_value = page.file_input.get_attribute("value")
        assert file_input_value, f"Файл не был выбран. Значение input: '{file_input_value}'"

        page.click_upload()

        assert page.is_upload_successful(), "Сообщение 'File Uploaded!' не появилось"
