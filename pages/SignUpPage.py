import random
from playwright.sync_api import Page
from pages.Header import Header

class SignUpPage(Header):
    def __init__(self, page: Page):
        super().__init__(page)
        self.new_user_signup_enscription = "//h2[text()=\"New User Signup!\"]"
        self.login_enscription = "//h2[text()=\"Login to your account\"]"
        self.email_login_field = "input[data-qa=\"login-email\"]"
        self.password_login_field = "input[data-qa=\"login-password\"]"
        self.login_button = "button[data-qa=\"login-button\"]"
        self.name_signup_field = "input[data-qa=\"signup-name\"]"
        self.email_signup_field = "input[data-qa=\"signup-email\"]"
        self.signup_button = "button[data-qa=\"signup-button\"]"
        self.account_information_enscription = "h2.title.text-center[style=\"color: #FE980F;\"] >> text=\"Enter Account Information\""
        self.title_signup_field1 = "input[id=\"id_gender1\"]"
        self.title_signup_field2 = "input[id=\"id_gender2\"]"
        self.password_signup_field = "input[id=\"password\"]"
        self.day_signup_field = "select[id=\"days\"]"
        self.day_options = f"{self.day_signup_field} option:not([value=''])"
        self.month_signup_field = "select[id=\"months\"]"
        self.month_options = f"{self.month_signup_field} option:not([value=''])"
        self.year_signup_field = "select[id=\"years\"]"
        self.year_options = f"{self.year_signup_field} option:not([value=''])"
        self.newsletter_signup_check = "input[id=\"newsletter\"]"
        self.offers_signup_check = "input[id=\"optin\"]"
        self.first_name_signup_field = "input[id=\"first_name\"]"
        self.last_name_signup_field = "input[id=\"last_name\"]"
        self.company_signup_field = "input[id=\"company\"]"
        self.address1_signup_field = "input[id=\"address1\"]"
        self.address2_signup_field = "input[id=\"address2\"]"
        self.country_signup_field = "select[id=\"country\"]"
        self.country_options = f"{self.country_signup_field} option:not([value=''])"
        self.state_signup_field = "input[id=\"state\"]"
        self.city_signup_field = "input[id=\"city\"]"
        self.zipcode_signup_field = "input[id=\"zipcode\"]"
        self.phone_signup_field = "input[id=\"mobile_number\"]"
        self.create_account_button = "button[data-qa=\"create-account\"]"
        self.account_created_enscription = "h2.title.text-center[style=\"color: green;\"] >> text=\"Account Created!\""
        self.continue_button = "a[data-qa=\"continue-button\"]"
        self.login_error = "p[style=\"color: red;\"]"

    def fillCountry(self):
        selected_country = random.choice(self.getElements(self.country_options))
        self.selectText(self.getElement(self.country_signup_field), self.getText(selected_country))

    def fillDateOfBirth(self):
        selected_day = random.choice(self.getElements(self.day_options))
        selected_month = random.choice(self.getElements(self.month_options))
        selected_year = random.choice(self.getElements(self.year_options))
        self.selectText(self.getElement(self.day_signup_field), self.getText(selected_day))
        self.selectText(self.getElement(self.month_signup_field), self.getText(selected_month))
        self.selectText(self.getElement(self.year_signup_field), self.getText(selected_year))

    def checkNewUserSignupEnscription(self):
        return self.isVisible(self.getElement(self.new_user_signup_enscription))
    
    def checkLoginEnscription(self):
        return self.isVisible(self.getElement(self.login_enscription))
    
    def fillEmailLoginField(self, value: str):
        self.inputText(self.getElement(self.email_login_field), value)

    def fillPasswordLoginField(self, value: str):
        self.inputText(self.getElement(self.password_login_field), value)

    def clickLoginButton(self):
        self.clickButton(self.getElement(self.login_button))

    def fillNameSignUpField(self, value: str):
        self.inputText(self.getElement(self.name_signup_field), value)
    
    def fillEmailSignUpField(self, value: str):
        self.inputText(self.getElement(self.email_signup_field), value)

    def clickSignUpButton(self):
        self.clickButton(self.getElement(self.signup_button))

    def checkAccountInformationEnscription(self):
        return self.isVisible(self.getElement(self.account_information_enscription))
    
    def chooseGender(self, option: bool):
        self.clickButton(self.getElement(self.title_signup_field1 if option else self.title_signup_field2))

    def fillPasswordSignUpField(self, value: str):
        self.inputText(self.getElement(self.password_signup_field), value)

    def checkNewsletterSignUp(self):
        self.clickButton(self.getElement(self.newsletter_signup_check))

    def checkOffersSignUp(self):
        self.clickButton(self.getElement(self.offers_signup_check))
    
    def fillFirstNameSignUpField(self, value: str):
        self.inputText(self.getElement(self.first_name_signup_field), value)

    def fillLastNameSignUpField(self, value: str):
        self.inputText(self.getElement(self.last_name_signup_field), value)
    
    def fillCompanySignUpField(self, value: str):
        self.inputText(self.getElement(self.company_signup_field), value)

    def fillAdress1SignUpField(self, value: str):
        self.inputText(self.getElement(self.address1_signup_field), value)

    def fillAdress2SignUpField(self, value: str):
        self.inputText(self.getElement(self.address2_signup_field), value)

    def fillStateSignUpField(self, value: str):
        self.inputText(self.getElement(self.state_signup_field), value)

    def fillCitySignUpField(self, value: str):
        self.inputText(self.getElement(self.city_signup_field), value)

    def fillZipcodeSignUpField(self, value: str):
        self.inputText(self.getElement(self.zipcode_signup_field), value)
    
    def fillPhoneSignUpField(self, value: str):
        self.inputText(self.getElement(self.phone_signup_field), value)

    def clickCreateAccountButton(self):
        self.clickButton(self.getElement(self.create_account_button))

    def checkAccountCreatedEnscription(self):
        return self.isVisible(self.getElement(self.account_created_enscription))
    
    def clickContinue(self):
        self.clickButton(self.getElement(self.continue_button))

    def getLoginError(self):
        return self.getText(self.getElement(self.login_error))