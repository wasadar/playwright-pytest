import pytest
import allure

def screenshot(page,case: int, step: int):
    allure.attach( body=page.screenshot(full_page=True), name="case " + str(case) + " step " + str(step), attachment_type=allure.attachment_type.PNG)