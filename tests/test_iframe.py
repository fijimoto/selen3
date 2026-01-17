from pages.frames_page import FramesPage
from pages.nested_frames_page import NestedFramesPage
from pages.demoqa_frames_page import DemoqaFramesPage


DEMOQA_URL = "https://demoqa.com/frames"


class TestIFrame:

    def test_nested_frames(self, browser):
        """Тест #8: Nested Frames – проверить Parent и Child frame"""
        frames_page = FramesPage(browser)

        browser.get(DEMOQA_URL)
        frames_page.click_nested_frames_menu()

        nested_page = NestedFramesPage(browser)
        assert nested_page.is_opened(), "Страница Nested Frames не открылась"

        parent_text = nested_page.get_parent_frame_text()
        assert "Parent frame" in parent_text, \
            f"Expected 'Parent frame' in text, Actual: '{parent_text}'"

        child_text = nested_page.get_child_frame_text()
        assert "Child Iframe" in child_text, \
            f"Expected 'Child Iframe' in text, Actual: '{child_text}'"

    def test_frames_text_match(self, browser):
        """Тест #8: Frames – текст верхнего и нижнего фрейма совпадает"""
        frames_page = FramesPage(browser)

        browser.get(DEMOQA_URL)
        frames_page.click_frames_menu()

        demoqa_frames = DemoqaFramesPage(browser)
        assert demoqa_frames.is_opened(), "Страница Frames не открылась"

        top_text = demoqa_frames.get_top_frame_text()
        bottom_text = demoqa_frames.get_bottom_frame_text()

        assert top_text == bottom_text, \
            f"Texts don't match. Top: '{top_text}', Bottom: '{bottom_text}'"
