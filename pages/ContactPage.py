from playwright.sync_api import Page
from pages.Header import Header
import os

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
        self.home_button = "a.btn.btn-success[href=\"/\"]"

    def checkGetInTouchEnscription(self):
        return self.isVisible(self.getElement(self.get_in_touch_enscription))

    def fillNameContactField(self, value: str):
        self.inputText(self.getElement(self.name_contact_field), value)

    def fillEmailContactField(self, value: str):
        self.inputText(self.getElement(self.email_contact_field), value)

    def fillSubjectContactField(self, value: str):
        self.inputText(self.getElement(self.subject_contact_field), value)

    def fillMessageContactField(self, value: str):
        self.inputText(self.getElement(self.message_contact_field), value)

    def loadFileToField(self, file_path: str):
        self.loadFile(self.getElement(self.file_contact_field), os.path.abspath(file_path))
    
    def clickSubmitButton(self):
        self.clickButton(self.getElement(self.submit_button))

    def checkSuccessMessage(self):
        return self.getText(self.getElement(self.success_message))
    
    def returnHome(self):
        self.clickButton(self.getElement(self.home_button))