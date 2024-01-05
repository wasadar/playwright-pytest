from playwright.sync_api import Page, ElementHandle
from pages.Header import Header

class TestCasesPage(Header):
    def __init__(self, page: Page):
        super().__init__(page)
        self.tests_header = "h2.title.text-center > b"