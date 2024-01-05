from playwright.sync_api import Page, ElementHandle
from pages.Header import Header

class HomePage(Header):
    def __init__(self, page: Page):
        super().__init__(page)
        self.practice_header = "//h2[contains(text(), \"Full-Fledged practice website for Automation Engineers\")]"
        self.account_deleted_enscription = "h2.title.text-center[style=\"color: green;\"] >> text=\"Account Deleted!\""
        self.continue_button = "a[data-qa=\"continue-button\"]"
        self.footer_text = "//h2[contains(text(), \"Subscription\")]"
        self.email_footer_field = "input[id=\"susbscribe_email\"]"
        self.arrow_button = "button.btn.btn-default[type=\"submit\"]"
        self.subscribe_message = "div.alert-success.alert"