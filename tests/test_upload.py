import os
import pytest

from pages.upload_page import UploadPage
from config_reader import ConfigReader

config = ConfigReader()


BASE_URL = config.base_url


@pytest.fixture
def test_file():
    """Фикстура для создания и удаления тестового файла"""
    file_name = "test_upload.txt"
    file_path = os.path.join(os.getcwd(), file_name)

    with open(file_path, "w") as f:
        f.write("Test file content for upload")

    yield file_path, file_name

    if os.path.exists(file_path):
        os.remove(file_path)


class TestUpload:

    def test_upload_file(self, browser, test_file):
        """Тест #11: Загрузить файл на страницу"""
        test_file_path, test_file_name = test_file
        page = UploadPage(browser)

        browser.get(f"{BASE_URL}/upload")
        assert page.is_opened(), "Страница Upload не открылась"

        page.upload_file(test_file_path)
        page.click_upload()

        assert page.is_upload_successful(), "Сообщение 'File Uploaded!' не появилось"

        uploaded_name = page.get_uploaded_file_name()
        assert uploaded_name == test_file_name, \
            f"Expected: '{test_file_name}', Actual: '{uploaded_name}'"
