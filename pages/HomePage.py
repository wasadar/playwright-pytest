from playwright.sync_api import Page
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
    
    def checkPraticeHeader(self):
        return self.isVisible(self.getElement(self.practice_header))
    
    def checkAccountDeletion(self):
        return self.isVisible(self.getElement(self.account_deleted_enscription))
    
    def checkFooterEnscription(self):
        return self.isVisible(self.getElement(self.footer_text))
    
    def clickContinue(self):
        self.clickButton(self.getElement(self.continue_button))

    def clickArrowButton(self):
        self.clickButton(self.getElement(self.arrow_button))

    def fillEmailFooterField(self, value: str):
        self.inputText(self.getElement(self.email_footer_field), value)

    def checkSubscribeMessage(self):
        return self.getText(self.getElement(self.subscribe_message))