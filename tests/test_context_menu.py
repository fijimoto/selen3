from pages.context_menu_page import ContextMenuPage
from config_reader import ConfigReader

config = ConfigReader()


BASE_URL = config.base_url


class TestContextMenu:

    def test_context_click_alert(self, browser):
        """Тест #4: ПКМ на область – появляется Alert"""
        page = ContextMenuPage(browser)
        expected_alert_text = "You selected a context menu"

        browser.get(f"{BASE_URL}/context_menu")
        assert page.is_opened(), "Страница Context Menu не открылась"

        page.right_click_hot_spot()

        actual_alert_text = browser.get_alert_text()
        assert actual_alert_text == expected_alert_text, \
            f"Expected: '{expected_alert_text}', Actual: '{actual_alert_text}'"

        browser.accept_alert()
