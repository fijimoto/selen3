from pages.base_page import BasePage
from elements.button import Button
from elements.label import Label


class AlertsPage(BasePage):
    PATH = "/javascript_alerts"

    UNIQUE_ELEMENT_LOC = "//h3[text()='JavaScript Alerts']"
    JS_ALERT_BUTTON_LOC = "//button[@onclick='jsAlert()']"
    JS_CONFIRM_BUTTON_LOC = "//button[@onclick='jsConfirm()']"
    JS_PROMPT_BUTTON_LOC = "//button[@onclick='jsPrompt()']"
    RESULT_LOC = "result"

    def __init__(self, browser):
        super().__init__(browser)

        self.page_name = "Alerts Page"

        self.unique_element = Label(
            self.browser,
            self.UNIQUE_ELEMENT_LOC,
            description="Alerts -> Header"
        )

        self.js_alert_button = Button(
            self.browser,
            self.JS_ALERT_BUTTON_LOC,
            description="Alerts -> JS Alert button"
        )

        self.js_confirm_button = Button(
            self.browser,
            self.JS_CONFIRM_BUTTON_LOC,
            description="Alerts -> JS Confirm button"
        )

        self.js_prompt_button = Button(
            self.browser,
            self.JS_PROMPT_BUTTON_LOC,
            description="Alerts -> JS Prompt button"
        )

        self.result = Label(
            self.browser,
            self.RESULT_LOC,
            description="Alerts -> Result text"
        )

    def click_js_alert(self) -> None:
        """Нажать кнопку JS Alert"""
        self.js_alert_button.click()

    def click_js_confirm(self) -> None:
        """Нажать кнопку JS Confirm"""
        self.js_confirm_button.click()

    def click_js_prompt(self) -> None:
        """Нажать кнопку JS Prompt"""
        self.js_prompt_button.click()

    def get_result_text(self) -> str:
        """Получить текст результата"""
        return self.result.get_text()
