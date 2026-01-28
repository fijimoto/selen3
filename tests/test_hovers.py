from pages.hovers_page import HoversPage
from pages.user_profile_page import UserProfilePage
from config_reader import ConfigReader

config = ConfigReader()


BASE_URL = config.base_url


class TestHovers:

    def test_hovers_all_users(self, browser):
        """Тест #6: Навести курсор на каждого пользователя и проверить профиль"""
        hovers_page = HoversPage(browser)

        browser.get(f"{BASE_URL}/hovers")
        assert hovers_page.is_opened(), "Страница Hovers не открылась"

        users_count = hovers_page.get_user_cards_count()

        for i in range(1, users_count + 1):
            hovers_page.hover_user(i)

            user_name = hovers_page.get_user_name(i)
            expected_name = f"name: user{i}"
            assert user_name == expected_name, \
                f"Expected: '{expected_name}', Actual: '{user_name}'"

            hovers_page.click_user_profile(i)

            profile_page = UserProfilePage(browser)
            assert profile_page.is_opened(), f"Профиль user{i} не открылся"

            user_id = browser.get_current_url().split("/")[-1]
            assert user_id == str(i), \
                f"Expected user ID: '{i}', Actual: '{user_id}'"

            browser.go_back()
            assert hovers_page.is_opened(), "Не удалось вернуться на страницу Hovers"
