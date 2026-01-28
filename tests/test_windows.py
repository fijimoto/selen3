from config_reader import ConfigReader
from pages.new_window_page import NewWindowPage
from pages.windows_page import WindowsPage

config = ConfigReader()


BASE_URL = config.base_url


class TestWindows:

    def test_window_handles(self, browser):
        """Тест #7: Работа с несколькими вкладками"""
        windows_page = WindowsPage(browser)
        expected_new_window_text = "New Window"
        expected_new_window_title = "New Window"

        browser.get(f"{BASE_URL}/windows")
        assert windows_page.is_opened(), "Страница Windows не открылась"

        handles_before = browser.get_window_handles()
        windows_page.click_link()
        browser.wait_for_new_window(handles_before)

        browser.switch_to_new_window()

        new_window_page = NewWindowPage(browser)
        assert new_window_page.is_opened(), "Новая вкладка не открылась"

        actual_text = new_window_page.get_header_text()
        assert actual_text == expected_new_window_text, \
            f"Expected: '{expected_new_window_text}', Actual: '{actual_text}'"

        actual_title = browser.get_title()
        assert actual_title == expected_new_window_title, \
            f"Expected title: '{expected_new_window_title}', Actual: '{actual_title}'"

        first_new_handle = browser.get_current_window_handle()

        browser.switch_to_main_window()
        assert windows_page.is_opened(), "Не удалось вернуться на главную страницу"

        handles_before = browser.get_window_handles()
        windows_page.click_link()
        browser.wait_for_new_window(handles_before)

        all_handles = browser.get_window_handles()
        for handle in all_handles:
            if handle != browser.main_handle and handle != first_new_handle:
                browser.switch_to_window_handle(handle)
                break

        new_window_page_2 = NewWindowPage(browser)
        assert new_window_page_2.is_opened(), "Вторая новая вкладка не открылась"

        actual_text_2 = new_window_page_2.get_header_text()
        assert actual_text_2 == expected_new_window_text, \
            f"Expected: '{expected_new_window_text}', Actual: '{actual_text_2}'"

        second_new_handle = browser.get_current_window_handle()

        browser.switch_to_main_window()
        assert windows_page.is_opened(), "Не удалось вернуться на главную страницу"

        browser.switch_to_window_handle(first_new_handle)
        browser.close()

        browser.switch_to_window_handle(second_new_handle)
        browser.close()

        browser.switch_to_main_window()
        assert windows_page.is_opened(), "Главная страница не доступна после закрытия вкладок"

        remaining_handles = browser.get_window_handles()
        assert len(remaining_handles) == 1, \
            f"Не все вкладки были закрыты. Осталось: {len(remaining_handles)}"
