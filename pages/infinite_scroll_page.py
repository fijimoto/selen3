from bs4 import BeautifulSoup

from elements.label import Label
from pages.base_page import BasePage


class InfiniteScrollPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//div//h3[contains(text(), 'Infinite Scroll')]"
    SCROLL_TEXT_LOC = "(//div[contains(@class, 'jscroll-added')])[last()]"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Infinity Scroll Page"
        self.unique_element = Label(browser, self.UNIQUE_ELEMENT_LOC, description="Unique_element page -> None")

        self.elements_text_loc = Label(browser, self.SCROLL_TEXT_LOC, description="Elements_text_loc -> None")

    def scroll_element(self, age):
        lst_paragraphs = []
        while True:
            self.elements_text_loc.wait_for_presence()
            self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            soup = BeautifulSoup(self.browser.driver.page_source, "html.parser")
            paragraphs = soup.find_all("div", class_="jscroll-added")

            for p in paragraphs:
                txt = p.get_text(strip=True)
                if txt and txt not in lst_paragraphs:
                    lst_paragraphs.append(txt)

            if len(lst_paragraphs) >= age:
                break

        return lst_paragraphs[:age]
