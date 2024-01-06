from playwright.sync_api import Page
from pages.HomePage import HomePage
from pages.SignUpPage import SignUpPage
from pages.ProductsPage import ProductsPage
from typing import Callable
from helpers.utils import screenshot

def stepsFrom1to3(page: Page, case, increment: Callable):
    home = HomePage(page)

    screenshot(page,case,increment())
    home.open()
    screenshot(page,case,increment())
    assert home.checkPraticeHeader() and home.ifHomeLinkIsOpened(), "Home page is not visible"
    screenshot(page,case,increment())

def step4AccountTests(page: Page, case, increment: Callable):
    home = HomePage(page)

    home.openLogin()
    screenshot(page,case,increment())

def stepsFrom5to7SignUp(page: Page, case, increment: Callable, name, email):
    sign_up = SignUpPage(page)

    assert sign_up.checkNewUserSignupEnscription(), "No new user sign up enscription"
    screenshot(page,case,increment())
    sign_up.fillNameSignUpField(name)
    sign_up.fillEmailSignUpField(email)
    screenshot(page,case,increment())
    sign_up.clickSignUpButton()
    screenshot(page,case,increment())

def stepsFrom5to7Login(page: Page, case, increment: Callable, email, password):
    sign_up = SignUpPage(page)

    assert sign_up.checkLoginEnscription(), "No login to your account enscription"
    screenshot(page,case,increment())
    sign_up.fillEmailLoginField(email)
    sign_up.fillPasswordLoginField(password)
    screenshot(page,case,increment())
    sign_up.clickLoginButton()
    screenshot(page,case,increment())

def verifyLogin(page: Page, case, increment: Callable):
    home = HomePage(page)

    assert home.ifUserIsLoggedIn(), "Logged in as enscription is not visible"
    screenshot(page,case,increment())

def deleteAccountAndVerifyDeletion(page: Page, case, increment: Callable):
    home = HomePage(page)

    home.deleteAccount()
    screenshot(page,case,increment())
    assert home.checkAccountDeletion() , "Account deleted enscription is not visible"
    screenshot(page,case,increment())

def stepsFrom4to5Products(page: Page, case, increment: Callable):
    home = HomePage(page)
    products = ProductsPage(page)

    home.openProducts()
    screenshot(page,case,increment())
    assert products.checkProductsEnscription(), "User is not navigated to all products page"
    screenshot(page,case,increment())