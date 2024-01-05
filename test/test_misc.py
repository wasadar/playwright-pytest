import pytest
import os
import allure
from faker import Faker
from playwright.sync_api import Page
from pages.HomePage import HomePage
from pages.ContactPage import ContactPage
from pages.TestCasesPage import TestCasesPage
from pages.ProductsPage import ProductsPage

fake = Faker()

def test_case_6(page: Page):
    home = HomePage(page)
    contact = ContactPage(page)
    
    home.open() # step 2
    allure.attach( body=page.screenshot(full_page=True), name="case 6 step 2", attachment_type=allure.attachment_type.PNG)
    practice_header = home.getElement(home.practice_header) # step 3
    home_link = home.getElement(home.home_link)
    assert home.isVisible(practice_header) and home.isOpened(home_link), "Home page is not visible"
    allure.attach( body=page.screenshot(full_page=True), name="case 6 step 3", attachment_type=allure.attachment_type.PNG)
    home.clickButton(home.getElement(home.concat_us_link)) # step 4
    allure.attach( body=page.screenshot(full_page=True), name="case 6 step 4", attachment_type=allure.attachment_type.PNG)
    get_in_touch_enscription = contact.getElement(contact.get_in_touch_enscription) # step 5
    assert contact.isVisible(get_in_touch_enscription), "Get in touch enscription is not visible"
    allure.attach( body=page.screenshot(full_page=True), name="case 6 step 5", attachment_type=allure.attachment_type.PNG)
    contact.inputText(contact.getElement(contact.name_contact_field), ''.join(fake.random_letters(6))) # step 6
    contact.inputText(contact.getElement(contact.email_contact_field), fake.email())
    contact.inputText(contact.getElement(contact.subject_contact_field), ''.join(fake.random_letters(15)))
    contact.inputText(contact.getElement(contact.message_contact_field), fake.text())
    allure.attach( body=page.screenshot(full_page=True), name="case 6 step 6", attachment_type=allure.attachment_type.PNG)
    contact.loadFile(contact.getElement(contact.file_contact_field), os.path.abspath("../file-for-loading.txt")) # step 7
    allure.attach( body=page.screenshot(full_page=True), name="case 6 step 7", attachment_type=allure.attachment_type.PNG)
    contact.clickButton(contact.getElement(contact.submit_button)) # step 8
    allure.attach( body=page.screenshot(full_page=True), name="case 6 step 8", attachment_type=allure.attachment_type.PNG)
    contact.acceptDialogue() # step 9
    allure.attach( body=page.screenshot(full_page=True), name="case 6 step 9", attachment_type=allure.attachment_type.PNG)
    success_message = contact.getElement(contact.success_message) # step 10
    assert contact.getText(success_message) == "Success! Your details have been submitted successfully.", "Success message is not shown or is wrong"
    allure.attach( body=page.screenshot(full_page=True), name="case 6 step 10", attachment_type=allure.attachment_type.PNG)
    contact.clickButton(contact.getElement(contact.home_button)) # step 11
    practice_header = home.getElement(home.practice_header)
    home_link = home.getElement(home.home_link)
    assert home.isVisible(practice_header) and home.isOpened(home_link), "Home page is not visible"
    allure.attach( body=page.screenshot(full_page=True), name="case 6 step 11", attachment_type=allure.attachment_type.PNG)

def test_case_7(page: Page):
    home = HomePage(page)
    tests = TestCasesPage(page)
    
    home.open() # step 2
    allure.attach( body=page.screenshot(full_page=True), name="case 7 step 2", attachment_type=allure.attachment_type.PNG)
    practice_header = home.getElement(home.practice_header) # step 3
    home_link = home.getElement(home.home_link)
    assert home.isVisible(practice_header) and home.isOpened(home_link), "Home page is not visible"
    allure.attach( body=page.screenshot(full_page=True), name="case 7 step 3", attachment_type=allure.attachment_type.PNG)
    home.clickButton(home.getElement(home.test_cases_link)) # step 4
    allure.attach( body=page.screenshot(full_page=True), name="case 7 step 4", attachment_type=allure.attachment_type.PNG)
    test_enscription = tests.getElement(tests.tests_header) # step 5
    assert tests.isVisible(test_enscription), "User is not navigated to test cases page"
    allure.attach( body=page.screenshot(full_page=True), name="case 7 step 5", attachment_type=allure.attachment_type.PNG)

def test_case_8(page: Page):
    home = HomePage(page)
    products = ProductsPage(page)

    home.open() # step 2
    allure.attach( body=page.screenshot(full_page=True), name="case 8 step 2", attachment_type=allure.attachment_type.PNG)
    practice_header = home.getElement(home.practice_header) # step 3
    home_link = home.getElement(home.home_link)
    assert home.isVisible(practice_header) and home.isOpened(home_link), "Home page is not visible"
    allure.attach( body=page.screenshot(full_page=True), name="case 8 step 3", attachment_type=allure.attachment_type.PNG)
    home.clickButton(home.getElement(home.products_link)) # step 4
    allure.attach( body=page.screenshot(full_page=True), name="case 8 step 4", attachment_type=allure.attachment_type.PNG)
    products_header = products.getElement(products.products_header) # step 5
    assert products.isVisible(products_header), "User is not navigated to all products page"
    allure.attach( body=page.screenshot(full_page=True), name="case 8 step 5", attachment_type=allure.attachment_type.PNG)
    products_list = products.getElement(products.products_list) # step 6
    assert products.isVisible(products_list), "Products list is not visible"
    allure.attach( body=page.screenshot(full_page=True), name="case 8 step 6", attachment_type=allure.attachment_type.PNG)
    products.clickButton(products.getElement(products.first_product_link)) # step 7
    allure.attach( body=page.screenshot(full_page=True), name="case 8 step 7", attachment_type=allure.attachment_type.PNG)
    product_details = products.getElement(products.product_details) # step 8
    assert products.isVisible(product_details), "User is not navigated to product detail page"
    allure.attach( body=page.screenshot(full_page=True), name="case 8 step 8", attachment_type=allure.attachment_type.PNG)
    name = products.getElement(products.name) # step 9
    category = products.getElement(products.category)
    price = products.getElement(products.price)
    availability = products.getElement(products.availability)
    condition = products.getElement(products.condition)
    brand = products.getElement(products.brand)
    assert products.isVisible(name) and products.isVisible(category) and products.isVisible(price) and products.isVisible(availability) and products.isVisible(condition) and products.isVisible(brand), "Something is wrong with products details"
    allure.attach( body=page.screenshot(full_page=True), name="case 8 step 9", attachment_type=allure.attachment_type.PNG)

def test_case_9(page: Page):
    home = HomePage(page)
    products = ProductsPage(page)
    
    home.open() # step 2
    allure.attach( body=page.screenshot(full_page=True), name="case 9 step 2", attachment_type=allure.attachment_type.PNG)
    practice_header = home.getElement(home.practice_header) # step 3
    home_link = home.getElement(home.home_link)
    assert home.isVisible(practice_header) and home.isOpened(home_link), "Home page is not visible"
    allure.attach( body=page.screenshot(full_page=True), name="case 9 step 3", attachment_type=allure.attachment_type.PNG)
    home.clickButton(home.getElement(home.products_link)) # step 4
    allure.attach( body=page.screenshot(full_page=True), name="case 9 step 4", attachment_type=allure.attachment_type.PNG)
    products_header = products.getElement(products.products_header) # step 5
    assert products.isVisible(products_header), "User is not navigated to all products page"
    allure.attach( body=page.screenshot(full_page=True), name="case 9 step 5", attachment_type=allure.attachment_type.PNG)
    products.inputText(products.getElement(products.search_field), "Blue Top") # step 6 
    # here is used hardcode instead of generation value cause otherwise there is probablity that there wouldn't be such products which will fail the test in next steps
    products.clickButton(products.getElement(products.search_button))
    allure.attach( body=page.screenshot(full_page=True), name="case 9 step 6", attachment_type=allure.attachment_type.PNG)
    searched_products_header = products.getElement(products.searched_products_header) # step 7
    assert products.isVisible(searched_products_header), "Searched products enscription is not visible"
    allure.attach( body=page.screenshot(full_page=True), name="case 9 step 7", attachment_type=allure.attachment_type.PNG)
    product_block = products.getElement(products.product_block) # step 8
    product_name = products.getElement(products.product_name)
    assert products.isVisible(product_block) and products.isVisible(product_name), "Related product is not visible"
    allure.attach( body=page.screenshot(full_page=True), name="case 9 step 8", attachment_type=allure.attachment_type.PNG)

def test_case_10(page: Page):
    home = HomePage(page)
    
    home.open() # step 2
    allure.attach( body=page.screenshot(full_page=True), name="case 10 step 2", attachment_type=allure.attachment_type.PNG)
    practice_header = home.getElement(home.practice_header) # step 3
    home_link = home.getElement(home.home_link)
    assert home.isVisible(practice_header) and home.isOpened(home_link), "Home page is not visible"
    allure.attach( body=page.screenshot(full_page=True), name="case 10 step 3", attachment_type=allure.attachment_type.PNG)
    home.scrollToFooter() #step 4
    allure.attach( body=page.screenshot(full_page=True), name="case 10 step 4", attachment_type=allure.attachment_type.PNG)
    footer_text = home.getElement(home.footer_text) # step 5
    assert home.isVisible(footer_text), "Subscription is not visible"
    allure.attach( body=page.screenshot(full_page=True), name="case 10 step 5", attachment_type=allure.attachment_type.PNG)
    home.inputText(home.getElement(home.email_footer_field), fake.email()) # step 6
    home.clickButton(home.getElement(home.arrow_button))
    allure.attach( body=page.screenshot(full_page=True), name="case 10 step 6", attachment_type=allure.attachment_type.PNG)
    subscribe_message = home.getElement(home.subscribe_message) # step 7
    assert home.getText(subscribe_message) == "You have been successfully subscribed!", "Success message is not shown or is wrong"
    allure.attach( body=page.screenshot(full_page=True), name="case 10 step 7", attachment_type=allure.attachment_type.PNG)
