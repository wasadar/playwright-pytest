import pytest
from playwright.sync_api import Page
from pages.HomePage import HomePage
from pages.SignUpPage import SignUpPage
from helpers.fixtures import random_string_generator, random_mail_generator, \
        random_address_generator, random_boolean_generator, random_city_generator, \
        random_phone_generator, random_postcode_generator, random_state_generator, \
        increment
from helpers.repeating_steps import stepsFrom1to3, step4AccountTests, stepsFrom5to7SignUp, \
    stepsFrom5to7Login, verifyLogin, deleteAccountAndVerifyDeletion
from helpers.utils import screenshot

@pytest.fixture
def registered_user(page, random_string_generator, random_mail_generator, random_address_generator, \
    random_boolean_generator, random_city_generator, random_phone_generator, random_postcode_generator, random_state_generator):
    home = HomePage(page)
    sign_up = SignUpPage(page)

    name = random_string_generator(6)
    email = random_mail_generator()
    password = random_string_generator(6)

    home.open()
    home.openLogin()
    sign_up.fillNameSignUpField(name)
    sign_up.fillEmailSignUpField(email)
    sign_up.clickSignUpButton()
    sign_up.chooseGender(random_boolean_generator())
    sign_up.fillPasswordSignUpField(password)
    sign_up.fillDateOfBirth()
    sign_up.checkNewsletterSignUp()
    sign_up.checkOffersSignUp()
    sign_up.fillFirstNameSignUpField(random_string_generator(6))
    sign_up.fillLastNameSignUpField(random_string_generator(6)) 
    sign_up.fillCompanySignUpField(random_string_generator(6))
    sign_up.fillAdress1SignUpField(random_address_generator())
    sign_up.fillAdress2SignUpField(random_address_generator())
    sign_up.fillCountry()
    sign_up.fillStateSignUpField(random_state_generator())
    sign_up.fillCitySignUpField(random_city_generator())
    sign_up.fillZipcodeSignUpField(random_postcode_generator())
    sign_up.fillPhoneSignUpField(random_phone_generator())
    sign_up.clickCreateAccountButton()
    sign_up.clickContinue()
    home.logout()

    return {"username": name, "email": email, "password": password}


def test_case_1(page: Page, random_string_generator, random_mail_generator, random_address_generator, \
    random_boolean_generator, random_city_generator, random_phone_generator, random_postcode_generator, \
    random_state_generator, increment):
    home = HomePage(page)
    sign_up = SignUpPage(page)
    case = 1
    
    stepsFrom1to3(page,case,increment) # steps 1 - 3
    step4AccountTests(page,case,increment) # step 4
    stepsFrom5to7SignUp(page,case,increment, random_string_generator(6), random_mail_generator()) # steps 5 - 7

    assert sign_up.checkAccountInformationEnscription(), "Enter account information enscreption is not visible" # step 8
    screenshot(page,case,increment())
    sign_up.chooseGender(random_boolean_generator()) # step 9
    sign_up.fillPasswordSignUpField(random_string_generator(6))
    sign_up.fillDateOfBirth()
    screenshot(page,case,increment())
    sign_up.checkNewsletterSignUp() # step 10
    screenshot(page,case,increment())
    sign_up.checkOffersSignUp() # step 11
    screenshot(page,case,increment())
    sign_up.fillFirstNameSignUpField(random_string_generator(6)) # step 12
    sign_up.fillLastNameSignUpField(random_string_generator(6)) 
    sign_up.fillCompanySignUpField(random_string_generator(6))
    sign_up.fillAdress1SignUpField(random_address_generator())
    sign_up.fillAdress2SignUpField(random_address_generator())
    sign_up.fillCountry()
    sign_up.fillStateSignUpField(random_state_generator())
    sign_up.fillCitySignUpField(random_city_generator())
    sign_up.fillZipcodeSignUpField(random_postcode_generator())
    sign_up.fillPhoneSignUpField(random_phone_generator())
    screenshot(page,case,increment())
    sign_up.clickCreateAccountButton() # step 13
    screenshot(page,case,increment())
    assert sign_up.checkAccountCreatedEnscription() #step 14
    screenshot(page,case,increment())
    sign_up.clickContinue() # step 15
    screenshot(page,case,increment())

    verifyLogin(page,case,increment) # step 16
    deleteAccountAndVerifyDeletion(page,case,increment) # steps 17 - 18

def test_case_2(page: Page, registered_user, increment):
    case = 2

    stepsFrom1to3(page,case,increment) # steps 1 - 3
    step4AccountTests(page,case,increment) # step 4
    stepsFrom5to7Login(page,case,increment, registered_user['email'], registered_user['password']) # steps 5 - 7
    verifyLogin(page,case,increment) # step 8
    deleteAccountAndVerifyDeletion(page,case,increment) # steps 9 - 10

def test_case_3(page: Page, registered_user, random_string_generator, increment):
    sign_up = SignUpPage(page)
    case = 3
    
    stepsFrom1to3(page,case,increment) # steps 1 - 3
    step4AccountTests(page,case,increment) # step 4
    stepsFrom5to7Login(page,case,increment, registered_user['email'], random_string_generator(5)) # steps 5 - 7

    assert sign_up.getLoginError() == "Your email or password is incorrect!", "Error message is not shown or is wrong" # step 8
    screenshot(page,case,increment()) 

def test_case_4(page: Page, registered_user, increment):
    home = HomePage(page)
    sign_up = SignUpPage(page)
    case = 4

    stepsFrom1to3(page,case,increment) # steps 1 - 3
    step4AccountTests(page,case,increment) # step 4
    stepsFrom5to7Login(page,case,increment, registered_user['email'], registered_user['password']) # steps 5 - 7
    verifyLogin(page,case,increment) # step 8

    home.logout() # step 9
    screenshot(page,case,increment())
    assert sign_up.checkLoginEnscription() and sign_up.checkNewUserSignupEnscription(), "User is not redirected to login page" # step 10
    screenshot(page,case,increment())
    
def test_case_5(page: Page, registered_user, random_string_generator, increment):
    sign_up = SignUpPage(page)
    case = 5
    
    stepsFrom1to3(page,case,increment) # steps 1 - 3
    step4AccountTests(page,case,increment) # step 4
    screenshot(page,case,increment())
    stepsFrom5to7SignUp(page,case,increment, random_string_generator(6), registered_user['email']) # steps 5 - 7

    assert sign_up.getLoginError() == "Email Address already exist!", "Error message is not shown or is wrong" # step 8
    screenshot(page,case,increment()) 