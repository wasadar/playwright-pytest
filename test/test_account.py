import pytest
import random
import allure
from faker import Faker
from playwright.sync_api import Page
from pages.HomePage import HomePage
from pages.SignUpPage import SignUpPage

fake = Faker()

@pytest.fixture
def register_user(page):
    home = HomePage(page)
    sign_up = SignUpPage(page)

    name = ''.join(fake.random_letters(6))
    email = fake.email()
    password = ''.join(fake.random_letters(6))

    home.open()
    home.clickButton(home.getElement(home.login_link))
    sign_up.inputText(sign_up.getElement(sign_up.name_signup_field), name)
    sign_up.inputText(sign_up.getElement(sign_up.email_signup_field), email)
    sign_up.clickButton(sign_up.getElement(sign_up.signup_button))
    sign_up.clickButton(sign_up.getElement(random.choice([sign_up.title_signup_field1, sign_up.title_signup_field2])))
    sign_up.inputText(sign_up.getElement(sign_up.password_signup_field), password)
    sign_up.fillDateOfBirth()
    sign_up.clickButton(sign_up.getElement(sign_up.newsletter_signup_check))
    sign_up.clickButton(sign_up.getElement(sign_up.offers_signup_check))
    sign_up.inputText(sign_up.getElement(sign_up.first_name_signup_field), ''.join(fake.random_letters(6)))
    sign_up.inputText(sign_up.getElement(sign_up.last_name_signup_field), ''.join(fake.random_letters(6)))
    sign_up.inputText(sign_up.getElement(sign_up.company_signup_field), ''.join(fake.random_letters(6)))
    sign_up.inputText(sign_up.getElement(sign_up.address1_signup_field), fake.address())
    sign_up.inputText(sign_up.getElement(sign_up.address2_signup_field), fake.address())
    sign_up.fillCountry()
    sign_up.inputText(sign_up.getElement(sign_up.state_signup_field), fake.state())
    sign_up.inputText(sign_up.getElement(sign_up.city_signup_field), fake.city())
    sign_up.inputText(sign_up.getElement(sign_up.zipcode_signup_field), fake.postcode())
    sign_up.inputText(sign_up.getElement(sign_up.phone_signup_field), fake.phone_number())
    sign_up.clickButton(sign_up.getElement(sign_up.create_account_button))
    sign_up.clickButton(sign_up.getElement(sign_up.continue_button))
    home.clickButton(home.getElement(home.logout_link))

    return {"username": name, "email": email, "password": password}


def test_case_1(page: Page):
    home = HomePage(page)
    sign_up = SignUpPage(page)
    
    home.open() # step 2
    allure.attach( body=page.screenshot(full_page=True), name="case 1 step 2", attachment_type=allure.attachment_type.PNG)
    practice_header = home.getElement(home.practice_header) # step 3
    home_link = home.getElement(home.home_link)
    assert home.isVisible(practice_header) and home.isOpened(home_link), "Home page is not visible"
    allure.attach( body=page.screenshot(full_page=True), name="case 1 step 3", attachment_type=allure.attachment_type.PNG)
    home.clickButton(home.getElement(home.login_link)) # step 4
    allure.attach( body=page.screenshot(full_page=True), name="case 1 step 4", attachment_type=allure.attachment_type.PNG)
    new_user_signup_enscription = sign_up.getElement(sign_up.new_user_signup_enscription) # step 5
    assert sign_up.isVisible(new_user_signup_enscription), "No new user sign up enscription"
    allure.attach( body=page.screenshot(full_page=True), name="case 1 step 5", attachment_type=allure.attachment_type.PNG)
    sign_up.inputText(sign_up.getElement(sign_up.name_signup_field), ''.join(fake.random_letters(6))) # step 6
    sign_up.inputText(sign_up.getElement(sign_up.email_signup_field), fake.email())
    allure.attach( body=page.screenshot(full_page=True), name="case 1 step 6", attachment_type=allure.attachment_type.PNG)
    sign_up.clickButton(sign_up.getElement(sign_up.signup_button)) # step 7
    allure.attach( body=page.screenshot(full_page=True), name="case 1 step 7", attachment_type=allure.attachment_type.PNG)
    account_information_enscription = sign_up.getElement(sign_up.account_information_enscription) # step 8
    assert sign_up.isVisible(account_information_enscription), "Enter account information enscreption is not visible"
    allure.attach( body=page.screenshot(full_page=True), name="case 1 step 8", attachment_type=allure.attachment_type.PNG)
    sign_up.clickButton(sign_up.getElement(random.choice([sign_up.title_signup_field1,sign_up.title_signup_field2]))) # step 9
    sign_up.inputText(sign_up.getElement(sign_up.password_signup_field), ''.join(fake.random_letters(6)))
    sign_up.fillDateOfBirth()
    allure.attach( body=page.screenshot(full_page=True), name="case 1 step 9", attachment_type=allure.attachment_type.PNG)
    sign_up.clickButton(sign_up.getElement(sign_up.newsletter_signup_check)) # step 10
    allure.attach( body=page.screenshot(full_page=True), name="case 1 step 10", attachment_type=allure.attachment_type.PNG)
    sign_up.clickButton(sign_up.getElement(sign_up.offers_signup_check)) # step 11
    allure.attach( body=page.screenshot(full_page=True), name="case 1 step 11", attachment_type=allure.attachment_type.PNG)
    sign_up.inputText(sign_up.getElement(sign_up.first_name_signup_field), ''.join(fake.random_letters(6))) # step 12
    sign_up.inputText(sign_up.getElement(sign_up.last_name_signup_field), ''.join(fake.random_letters(6))) 
    sign_up.inputText(sign_up.getElement(sign_up.company_signup_field), ''.join(fake.random_letters(6)))
    sign_up.inputText(sign_up.getElement(sign_up.address1_signup_field), fake.address())
    sign_up.inputText(sign_up.getElement(sign_up.address2_signup_field), fake.address())
    sign_up.fillCountry()
    sign_up.inputText(sign_up.getElement(sign_up.state_signup_field), fake.state())
    sign_up.inputText(sign_up.getElement(sign_up.city_signup_field), fake.city())
    sign_up.inputText(sign_up.getElement(sign_up.zipcode_signup_field), fake.postcode())
    sign_up.inputText(sign_up.getElement(sign_up.phone_signup_field), fake.phone_number())
    allure.attach( body=page.screenshot(full_page=True), name="case 1 step 12", attachment_type=allure.attachment_type.PNG)
    sign_up.clickButton(sign_up.getElement(sign_up.create_account_button)) # step 13
    allure.attach( body=page.screenshot(full_page=True), name="case 1 step 13", attachment_type=allure.attachment_type.PNG)
    account_created_enscription = sign_up.getElement(sign_up.account_created_enscription) #step 14
    assert sign_up.isVisible(account_created_enscription)
    allure.attach( body=page.screenshot(full_page=True), name="case 1 step 14", attachment_type=allure.attachment_type.PNG)
    sign_up.clickButton(sign_up.getElement(sign_up.continue_button)) # step 15
    allure.attach( body=page.screenshot(full_page=True), name="case 1 step 15", attachment_type=allure.attachment_type.PNG)
    logged_in_enscription = home.getElement(home.logged_in_enscription) # step 16
    assert home.isVisible(logged_in_enscription), "Logged in as enscription is not visible"
    allure.attach( body=page.screenshot(full_page=True), name="case 1 step 16", attachment_type=allure.attachment_type.PNG)
    home.clickButton(home.getElement(home.delete_account_link)) # step 17
    allure.attach( body=page.screenshot(full_page=True), name="case 1 step 17", attachment_type=allure.attachment_type.PNG)
    account_deleted_enscription = home.getElement(home.account_deleted_enscription) # step 18
    assert home.isVisible(account_deleted_enscription), "Account deleted enscription is not visible"
    allure.attach( body=page.screenshot(full_page=True), name="case 1 step 18", attachment_type=allure.attachment_type.PNG)

def test_case_2(page: Page, register_user):
    home = HomePage(page)
    sign_up = SignUpPage(page)
    
    home.open() # step 2
    allure.attach( body=page.screenshot(full_page=True), name="case 2 step 2", attachment_type=allure.attachment_type.PNG)
    practice_header = home.getElement(home.practice_header) # step 3
    home_link = home.getElement(home.home_link)
    assert home.isVisible(practice_header) and home.isOpened(home_link), "Home page is not visible"
    allure.attach( body=page.screenshot(full_page=True), name="case 2 step 3", attachment_type=allure.attachment_type.PNG)
    home.clickButton(home.getElement(home.login_link)) # step 4
    allure.attach( body=page.screenshot(full_page=True), name="case 2 step 4", attachment_type=allure.attachment_type.PNG)
    login_enscription = sign_up.getElement(sign_up.login_enscription) # step 5
    assert sign_up.isVisible(login_enscription), "No login to your account enscription"
    allure.attach( body=page.screenshot(full_page=True), name="case 2 step 5", attachment_type=allure.attachment_type.PNG)
    sign_up.inputText(sign_up.getElement(sign_up.email_login_field), register_user["email"]) # step 6
    sign_up.inputText(sign_up.getElement(sign_up.password_login_field), register_user["password"])
    allure.attach( body=page.screenshot(full_page=True), name="case 2 step 6", attachment_type=allure.attachment_type.PNG)
    sign_up.clickButton(sign_up.getElement(sign_up.login_button)) # step 7
    allure.attach( body=page.screenshot(full_page=True), name="case 2 step 7", attachment_type=allure.attachment_type.PNG)
    logged_in_enscription = home.getElement(home.logged_in_enscription) # step 8
    assert home.isVisible(logged_in_enscription), "Logged in as enscription is not visible"
    allure.attach( body=page.screenshot(full_page=True), name="case 2 step 8", attachment_type=allure.attachment_type.PNG)
    home.clickButton(home.getElement(home.delete_account_link)) # step 9
    allure.attach( body=page.screenshot(full_page=True), name="case 2 step 9", attachment_type=allure.attachment_type.PNG)
    account_deleted_enscription = home.getElement(home.account_deleted_enscription) # step 10
    assert home.isVisible(account_deleted_enscription), "Account deleted enscription is not visible"
    allure.attach( body=page.screenshot(full_page=True), name="case 2 step 10", attachment_type=allure.attachment_type.PNG)

def test_case_3(page: Page, register_user):
    home = HomePage(page)
    sign_up = SignUpPage(page)
    
    home.open() # step 2
    allure.attach( body=page.screenshot(full_page=True), name="case 3 step 2", attachment_type=allure.attachment_type.PNG)
    practice_header = home.getElement(home.practice_header) # step 3
    home_link = home.getElement(home.home_link)
    assert home.isVisible(practice_header) and home.isOpened(home_link), "Home page is not visible"
    allure.attach( body=page.screenshot(full_page=True), name="case 3 step 3", attachment_type=allure.attachment_type.PNG)
    home.clickButton(home.getElement(home.login_link)) # step 4
    allure.attach( body=page.screenshot(full_page=True), name="case 3 step 4", attachment_type=allure.attachment_type.PNG)
    login_enscription = sign_up.getElement(sign_up.login_enscription) # step 5
    assert sign_up.isVisible(login_enscription), "No login to your account enscription"
    allure.attach( body=page.screenshot(full_page=True), name="case 3 step 5", attachment_type=allure.attachment_type.PNG)
    sign_up.inputText(sign_up.getElement(sign_up.email_login_field), register_user["email"]) # step 6
    sign_up.inputText(sign_up.getElement(sign_up.password_login_field), ''.join(fake.random_letters(5)))
    allure.attach( body=page.screenshot(full_page=True), name="case 3 step 6", attachment_type=allure.attachment_type.PNG)
    sign_up.clickButton(sign_up.getElement(sign_up.login_button)) # step 7
    allure.attach( body=page.screenshot(full_page=True), name="case 3 step 7", attachment_type=allure.attachment_type.PNG)
    error_message = sign_up.getElement(sign_up.login_error) # step 8
    assert sign_up.getText(error_message) == "Your email or password is incorrect!", "Error message is not shown or is wrong"
    allure.attach( body=page.screenshot(full_page=True), name="case 3 step 8", attachment_type=allure.attachment_type.PNG) 

def test_case_4(page: Page, register_user):
    home = HomePage(page)
    sign_up = SignUpPage(page)
    
    home.open() # step 2
    allure.attach( body=page.screenshot(full_page=True), name="case 4 step 2", attachment_type=allure.attachment_type.PNG) 
    practice_header = home.getElement(home.practice_header) # step 3
    home_link = home.getElement(home.home_link)
    assert home.isVisible(practice_header) and home.isOpened(home_link), "Home page is not visible"
    allure.attach( body=page.screenshot(full_page=True), name="case 4 step 2", attachment_type=allure.attachment_type.PNG) 
    home.clickButton(home.getElement(home.login_link)) # step 4
    allure.attach( body=page.screenshot(full_page=True), name="case 4 step 4", attachment_type=allure.attachment_type.PNG) 
    login_enscription = sign_up.getElement(sign_up.login_enscription) # step 5
    assert sign_up.isVisible(login_enscription), "No login to your account enscription"
    allure.attach( body=page.screenshot(full_page=True), name="case 4 step 5", attachment_type=allure.attachment_type.PNG) 
    sign_up.inputText(sign_up.getElement(sign_up.email_login_field), register_user["email"]) # step 6
    sign_up.inputText(sign_up.getElement(sign_up.password_login_field), register_user["password"])
    allure.attach( body=page.screenshot(full_page=True), name="case 4 step 6", attachment_type=allure.attachment_type.PNG) 
    sign_up.clickButton(sign_up.getElement(sign_up.login_button)) # step 7
    allure.attach( body=page.screenshot(full_page=True), name="case 4 step 7", attachment_type=allure.attachment_type.PNG) 
    logged_in_enscription = home.getElement(home.logged_in_enscription) # step 8
    assert home.isVisible(logged_in_enscription), "Logged in as enscription is not visible"
    allure.attach( body=page.screenshot(full_page=True), name="case 4 step 8", attachment_type=allure.attachment_type.PNG) 
    home.clickButton(home.getElement(home.logout_link)) # step 9
    allure.attach( body=page.screenshot(full_page=True), name="case 4 step 9", attachment_type=allure.attachment_type.PNG) 
    new_user_signup_enscription = sign_up.getElement(sign_up.new_user_signup_enscription) # step 10
    login_enscription = sign_up.getElement(sign_up.login_enscription) 
    assert sign_up.isVisible(new_user_signup_enscription) and sign_up.isVisible(login_enscription) , "User is not redirected to login page"
    allure.attach( body=page.screenshot(full_page=True), name="case 4 step 10", attachment_type=allure.attachment_type.PNG) 

def test_case_5(page: Page, register_user):
    home = HomePage(page)
    sign_up = SignUpPage(page)
    
    home.open() # step 2
    allure.attach( body=page.screenshot(full_page=True), name="case 5 step 2", attachment_type=allure.attachment_type.PNG) 
    practice_header = home.getElement(home.practice_header) # step 3
    home_link = home.getElement(home.home_link)
    assert home.isVisible(practice_header) and home.isOpened(home_link), "Home page is not visible"
    allure.attach( body=page.screenshot(full_page=True), name="case 5 step 3", attachment_type=allure.attachment_type.PNG) 
    home.clickButton(home.getElement(home.login_link)) # step 4
    allure.attach( body=page.screenshot(full_page=True), name="case 5 step 4", attachment_type=allure.attachment_type.PNG) 
    new_user_signup_enscription = sign_up.getElement(sign_up.new_user_signup_enscription) # step 5
    assert sign_up.isVisible(new_user_signup_enscription), "No new user sign up enscription"
    allure.attach( body=page.screenshot(full_page=True), name="case 5 step 5", attachment_type=allure.attachment_type.PNG) 
    sign_up.inputText(sign_up.getElement(sign_up.name_signup_field), register_user["username"]) # step 6
    sign_up.inputText(sign_up.getElement(sign_up.email_signup_field), register_user["email"])
    allure.attach( body=page.screenshot(full_page=True), name="case 5 step 6", attachment_type=allure.attachment_type.PNG) 
    sign_up.clickButton(sign_up.getElement(sign_up.signup_button)) # step 7
    allure.attach( body=page.screenshot(full_page=True), name="case 5 step 7", attachment_type=allure.attachment_type.PNG) 
    error_message = sign_up.getElement(sign_up.login_error) # step 8
    assert sign_up.getText(error_message) == "Email Address already exist!", "Error message is not shown or is wrong"
    allure.attach( body=page.screenshot(full_page=True), name="case 5 step 8", attachment_type=allure.attachment_type.PNG) 