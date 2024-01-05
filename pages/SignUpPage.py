import random
from playwright.sync_api import Page, ElementHandle
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
