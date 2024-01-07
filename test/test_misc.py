import pytest
from playwright.sync_api import Page
from pages.HomePage import HomePage
from pages.ContactPage import ContactPage
from pages.TestCasesPage import TestCasesPage
from pages.ProductsPage import ProductsPage
from helpers.fixtures import random_string_generator, random_mail_generator, random_text_generator, increment
from helpers.repeating_steps import stepsFrom1to3, stepsFrom4to5Products
from helpers.utils import screenshot

def test_case_6(page: Page, random_string_generator, random_mail_generator, random_text_generator, increment):
    home = HomePage(page)
    contact = ContactPage(page)
    case = 6
    
    stepsFrom1to3(page,case,increment) # steps 1 - 3

    home.openContactUs() # step 4
    screenshot(page,case,increment())
    assert contact.checkGetInTouchEnscription(), "Get in touch enscription is not visible" # step 5
    screenshot(page,case,increment())
    contact.fillNameContactField(random_string_generator(6)) # step 6
    contact.fillEmailContactField(random_mail_generator())
    contact.fillSubjectContactField(random_string_generator(15))
    contact.fillMessageContactField(random_text_generator())
    screenshot(page,case,increment())
    contact.loadFileToField("../file-for-loading.txt") # step 7
    screenshot(page,case,increment())
    contact.clickSubmitButton() # step 8
    screenshot(page,case,increment())
    contact.acceptDialogue() # step 9
    screenshot(page,case,increment())
    contact.clickSubmitButton() # bug-fix for steps 8-9
    assert contact.checkSuccessMessage() == "Success! Your details have been submitted successfully.", "Success message is not shown or is wrong" # step 10
    screenshot(page,case,increment())
    contact.returnHome() # step 11
    assert home.checkPraticeHeader() and home.ifHomeLinkIsOpened(), "Home page is not visible"
    screenshot(page,case,increment())

def test_case_7(page: Page, increment):
    home = HomePage(page)
    tests = TestCasesPage(page)
    case = 7
    
    stepsFrom1to3(page,case,increment) # steps 1 - 3

    home.openTestCases() # step 4
    screenshot(page,case,increment())
    assert tests.checkTestsHeader(), "User is not navigated to test cases page" # step 5
    screenshot(page,case,increment())

def test_case_8(page: Page, increment):
    products = ProductsPage(page)
    case = 8

    stepsFrom1to3(page,case,increment) # steps 1 - 3
    stepsFrom4to5Products(page,case,increment) # steps 4 - 5

    assert products.checkProductsList(), "Products list is not visible" # step 6
    screenshot(page,case,increment())
    products.clickFirstProductLink() # step 7
    screenshot(page,case,increment())
    assert products.checkProductDetails(), "User is not navigated to product detail page" # step 8
    screenshot(page,case,increment())
    name = products.checkProductDetailsName() # step 9
    category = products.checkProductDetailsCategory()
    price = products.checkProductDetailsPrice()
    availability = products.checkProductDetailsAvailability()
    condition = products.checkProductDetailsCondition()
    brand = products.checkProductDetailsBrand()
    assert name and category and price and availability and condition and brand, "Something is wrong with products details"
    screenshot(page,case,increment())

def test_case_9(page: Page, increment):
    products = ProductsPage(page)
    case = 9
    
    stepsFrom1to3(page,case,increment) # steps 1 - 3
    stepsFrom4to5Products(page,case,increment) # steps 4 - 5

    products.fillSearchRequest("Blue Top") # step 6 
    # here is used hardcode instead of generation value cause otherwise there is probablity that there wouldn't be such products which will fail the test in next steps
    products.clickSearchButton()
    screenshot(page,case,increment())
    assert products.checkSearchedProductsEnscription(), "Searched products enscription is not visible" # step 7
    screenshot(page,case,increment())
    assert products.checkProductBlock() and products.checkProductName(), "Related product is not visible" # step 8
    screenshot(page,case,increment())

def test_case_10(page: Page, random_mail_generator, increment):
    home = HomePage(page)
    case = 10
    
    stepsFrom1to3(page,case,increment) # steps 1 - 3

    home.scrollToFooter() #step 4
    screenshot(page,case,increment())
    assert home.checkFooterEnscription(), "Subscription is not visible" # step 5
    screenshot(page,case,increment())
    home.fillEmailFooterField(random_mail_generator()) # step 6
    home.clickArrowButton()
    screenshot(page,case,increment())
    assert home.checkSubscribeMessage() == "You have been successfully subscribed!", "Success message is not shown or is wrong" # step 7
    screenshot(page,case,increment())