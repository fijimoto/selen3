from pages.basic_auth_page import BasicAuthPage


class TestBasicAuth:

    def test_basic_auth_success(self, browser):
        """Тест #1: Basic Authorization"""
        page = BasicAuthPage(browser)
        expected_text = "Congratulations! You must have the proper credentials."

        username = "admin"
        password = "admin"

        browser.get(
            f"http://{username}:{password}@the-internet.herokuapp.com{page.PATH}")

        assert page.is_opened(), "Страница не открылась после авторизации"

        actual_text = page.get_content_text()
        assert expected_text in actual_text, \
            f"Expected: '{expected_text}', Actual: '{actual_text}'"
