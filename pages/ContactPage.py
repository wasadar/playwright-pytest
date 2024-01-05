from playwright.sync_api import Page, ElementHandle
from pages.Header import Header

class ContactPage(Header):
    def __init__(self, page: Page):
        super().__init__(page)
        self.get_in_touch_enscription = "h2 >> text=\"Get In Touch\""
        self.name_contact_field = "input[data-qa=\"name\"]"
        self.email_contact_field = "input[data-qa=\"email\"]"
        self.subject_contact_field = "input[data-qa=\"subject\"]"
        self.message_contact_field = "textarea[data-qa=\"message\"]"
        self.file_contact_field = "input[name=\"upload_file\"]"
        self.submit_button = "input[data-qa=\"submit-button\"]"
        self.success_message = "div.alert-success.alert"
        self.home_button = "a.btn.btn-success[href=\"/\"][previewlistener=\"true\"]"