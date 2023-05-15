import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from Homework16CheckBoxes.pages.page_dynamic_button import PageDynamic


@pytest.mark.usefixtures('chrome')
class TestDynamicProperties:

    def setup_method(self):
        self.driver: WebDriver = self.driver
        self.page_dynamic_button = PageDynamic(self.driver).open()

    def test_enabled_button_v1(self):
        button = self.page_dynamic_button.enable_button_v1()
        assert button is True

    def test_enabled_button_v2(self):
        button = self.page_dynamic_button.enable_button_v2()
        assert button

    def test_color_button(self):
        button = self.page_dynamic_button.color_button()
        assert button.is_displayed()

    def test_visible_button(self):
        button = self.page_dynamic_button.visible_button()
        assert button.is_displayed()
