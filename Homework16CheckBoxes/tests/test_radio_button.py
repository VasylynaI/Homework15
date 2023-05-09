import pytest
from selenium.webdriver.remote.webdriver import WebDriver
import time

from Homework16CheckBoxes.pages.page_radio_button import PageRadioButton


@pytest.mark.usefixtures('chrome')
class TestCheckboxes:

    def setup_method(self):
        self.driver: WebDriver = self.driver
        self.page_radio_button = PageRadioButton(self.driver).open()

    def test_activate_yes_radio(self):
        self.page_radio_button.select_radio_button('yes')
        assert self.page_radio_button.is_selected_radio_button('yes')

    def test_activate_yes_button_var2(self):
        self.page_radio_button.select_radio_button('yes')
        assert self.page_radio_button.check_radio_button_text_status('yes')

    def test_get_radio_buttons_info(self):
        self.page_radio_button.select_radio_button('yes')
        print(len(self.page_radio_button.collect_buttons_info()) == 3)

    def test_activate_disabled_button(self):
        self.page_radio_button.enable_radio_button('no')
        self.page_radio_button.select_radio_button('no')
        assert self.page_radio_button.is_selected_radio_button('no')
