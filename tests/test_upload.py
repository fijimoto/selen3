import os
import sys
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


@pytest.mark.skipif(sys.platform == "linux", reason="pyautogui не работает в Linux/Docker")
class TestUpload:
    def test_upload_file(self, browser, test_file):
        """Тест #11: Загрузить файл на страницу"""
        test_file_path, test_file_name = test_file
        page = UploadPage(browser)