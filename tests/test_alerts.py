from faker import Faker

from pages.alerts_page import AlertsPage
from config_reader import ConfigReader

config = ConfigReader()


fake = Faker()
BASE_URL = config.base_url


class TestAlerts:

    def test_js_alert(self, browser):
        """Тест: JS Alert – нажать OK"""
        page = AlertsPage(browser)
        expected_alert_text = "I am a JS Alert"
        expected_result = "You successfully clicked an alert"

        browser.get(f"{BASE_URL}/javascript_alerts")
        assert page.is_opened(), "Страница Alerts не открылась"

        page.click_js_alert()

        actual_alert_text = browser.get_alert_text()
        assert actual_alert_text == expected_alert_text, \
            f"Expected: '{expected_alert_text}', Actual: '{actual_alert_text}'"

        browser.accept_alert()

        actual_result = page.get_result_text()
        assert actual_result == expected_result, \
            f"Expected: '{expected_result}', Actual: '{actual_result}'"

    def test_js_confirm_ok(self, browser):
        """Тест: JS Confirm – нажать OK"""
        page = AlertsPage(browser)
        expected_alert_text = "I am a JS Confirm"
        expected_result = "You clicked: Ok"

        browser.get(f"{BASE_URL}/javascript_alerts")
        assert page.is_opened(), "Страница Alerts не открылась"

        page.click_js_confirm()

        actual_alert_text = browser.get_alert_text()
        assert actual_alert_text == expected_alert_text, \
            f"Expected: '{expected_alert_text}', Actual: '{actual_alert_text}'"

        browser.accept_alert()

        actual_result = page.get_result_text()
        assert actual_result == expected_result, \
            f"Expected: '{expected_result}', Actual: '{actual_result}'"

    def test_js_prompt(self, browser):
        """Тест: JS Prompt – ввести текст и нажать OK"""
        page = AlertsPage(browser)
        expected_alert_text = "I am a JS prompt"
        random_text = fake.sentence(nb_words=3)

        browser.get(f"{BASE_URL}/javascript_alerts")
        assert page.is_opened(), "Страница Alerts не открылась"

        page.click_js_prompt()

        actual_alert_text = browser.get_alert_text()
        assert actual_alert_text == expected_alert_text, \
            f"Expected: '{expected_alert_text}', Actual: '{actual_alert_text}'"

        browser.send_keys_alert(random_text)
        browser.accept_alert()

        expected_result = f"You entered: {random_text}"
        actual_result = page.get_result_text()
        assert actual_result == expected_result, \
            f"Expected: '{expected_result}', Actual: '{actual_result}'"

    def test_js_alert_via_script(self, browser):
        """Тест: JS Alert через execute_script"""
        page = AlertsPage(browser)
        expected_alert_text = "I am a JS Alert"
        expected_result = "You successfully clicked an alert"

        browser.get(f"{BASE_URL}/javascript_alerts")
        assert page.is_opened(), "Страница Alerts не открылась"

        browser.execute_script("jsAlert()")

        actual_alert_text = browser.get_alert_text()
        assert actual_alert_text == expected_alert_text, \
            f"Expected: '{expected_alert_text}', Actual: '{actual_alert_text}'"

        browser.accept_alert()

        actual_result = page.get_result_text()
        assert actual_result == expected_result, \
            f"Expected: '{expected_result}', Actual: '{actual_result}'"

    def test_js_confirm_via_script(self, browser):
        """Тест: JS Confirm через execute_script"""
        page = AlertsPage(browser)
        expected_alert_text = "I am a JS Confirm"
        expected_result = "You clicked: Ok"

        browser.get(f"{BASE_URL}/javascript_alerts")
        assert page.is_opened(), "Страница Alerts не открылась"

        browser.execute_script("jsConfirm()")

        actual_alert_text = browser.get_alert_text()
        assert actual_alert_text == expected_alert_text, \
            f"Expected: '{expected_alert_text}', Actual: '{actual_alert_text}'"

        browser.accept_alert()

        actual_result = page.get_result_text()
        assert actual_result == expected_result, \
            f"Expected: '{expected_result}', Actual: '{actual_result}'"

    def test_js_prompt_via_script(self, browser):
        """Тест: JS Prompt через execute_script"""
        page = AlertsPage(browser)
        expected_alert_text = "I am a JS prompt"
        random_text = fake.sentence(nb_words=3)

        browser.get(f"{BASE_URL}/javascript_alerts")
        assert page.is_opened(), "Страница Alerts не открылась"

        browser.execute_script("jsPrompt()")

        actual_alert_text = browser.get_alert_text()
        assert actual_alert_text == expected_alert_text, \
            f"Expected: '{expected_alert_text}', Actual: '{actual_alert_text}'"

        browser.send_keys_alert(random_text)
        browser.accept_alert()

        expected_result = f"You entered: {random_text}"
        actual_result = page.get_result_text()
        assert actual_result == expected_result, \
            f"Expected: '{expected_result}', Actual: '{actual_result}'"
