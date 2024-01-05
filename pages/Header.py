from playwright.sync_api import Page, ElementHandle
from pages.BasePage import BasePage;

class Header(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.home_link = "//a[not(ancestor::div[contains(@class, \"logo\")]) and @href=\"/\"]"
        self.products_link = "a[href=\"/products\"]"
        self.cart_link = "a[href=\"/view_cart\"]"
        self.login_link = "a[href=\"/login\"]"
        self.test_cases_link = "a[href=\"/test_cases\"]"
        self.concat_us_link = "a[href=\"/contact_us\"]"
        self.logged_in_enscription = "a:has-text(\"Logged in as\")"
        self.logout_link = "a[href=\"/logout\"]"
        self.delete_account_link = "a[href=\"/delete_account\"]"

    def isOpened(self, selector: ElementHandle):
        return self.getStyle(selector) == "color: orange;"