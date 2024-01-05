from playwright.sync_api import Page, ElementHandle
from pages.Header import Header

class ProductsPage(Header):
    def __init__(self, page: Page):
        super().__init__(page)
        self.products_header = "//h2[contains(text(), \"All Products\")]"
        self.searched_products_header = "//h2[contains(text(), \"Searched Products\")]"
        self.products_list = "div.features_items"
        self.first_product_link = "div.col-sm-4 div.choose ul.nav li:first-child a"
        self.product_details = "div.product-details"
        self.name = "div.product-information h2"
        self.category = "p:has-text(\"Category:\")"
        self.price = "span > span"
        self.availability = "p:has-text(\"Availability:\")"
        self.condition = "p:has-text(\"Condition:\")"
        self.brand = "p:has-text(\"Brand:\")"
        self.search_field = "input[id=\"search_product\"]"
        self.search_button = "button[id=\"submit_search\"]"
        self.product_block = "div.single-products"
        self.product_name = "div.productinfo h2"