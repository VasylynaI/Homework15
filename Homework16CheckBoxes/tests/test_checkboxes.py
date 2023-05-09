import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from Homework16CheckBoxes.pages.page_checkbox import PageCheckbox

expand_elements_list = ['home', 'desktop', 'documents', 'office']
mark_elements_list = ['commands', 'general']


@pytest.mark.usefixtures('chrome')
class TestCheckboxes:

    def setup_method(self):
        self.driver: WebDriver = self.driver
        self.checkbox_page = PageCheckbox(self.driver).open()

    def test_checkboxes(self):
        for elem in expand_elements_list:
            self.checkbox_page.page_expand_folder(elem)
        for elem in mark_elements_list:
            self.checkbox_page.page_mark_folder(elem)
        pass
