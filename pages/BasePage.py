from playwright.sync_api import Page, ElementHandle

class BasePage():
    def __init__(self, page: Page):
        self.page = page

    def open(self, url: str = "https://www.automationexercise.com/"):
        self.page.goto(url)

    def clickButton(self, selector: ElementHandle):
        selector.click()

    def inputText(self, selector: ElementHandle, text: str):
        selector.fill(text)

    def selectText(self, selector: ElementHandle, value: str):
        selector.select_option(value)

    def getText(self, selector: ElementHandle) -> str:
        return selector.text_content()
    
    def loadFile(self, selector: ElementHandle, file_path: str):
        selector.set_input_files(file_path)

    def isVisible(self, selector: ElementHandle) -> bool:
        return selector.is_visible()
    
    def getStyle(self, selector: ElementHandle) -> str:
        return selector.get_attribute('style')

    def getElement(self, selector: str) -> ElementHandle:
        return self.page.query_selector(selector)
    
    def getElements(self, selector: str):
        return self.page.query_selector_all(selector)
    
    def acceptDialogue(self):
        self.page.on("dialog", lambda dialog: dialog.accept())

    def scrollToFooter(self):
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
