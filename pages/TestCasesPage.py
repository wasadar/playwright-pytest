from playwright.sync_api import Page
from pages.Header import Header

class TestCasesPage(Header):
    def __init__(self, page: Page):
        super().__init__(page)
        self.tests_header = "h2.title.text-center > b"

    def checkTestsHeader(self):
        return self.isVisible(self.getElement(self.tests_header))