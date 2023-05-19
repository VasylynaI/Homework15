import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from Homework16CheckBoxes.pages.page_dynamic_button import PageDynamic


@pytest.mark.usefixtures('chrome')
class TestDynamicProperties:

    def setup_method(self):
        self.driver: WebDriver = self.driver
        self.page = PageDynamic(self.driver).open()

    def test_disabled_enabled_button_v1(self):
        button = self.page.button_disabled_enabled_v1()
        assert button is True

    def test_disabled_enabled_button_v2(self):
        button = self.page.button_disabled_enabled_v2()
        assert button

    def test_color_changed_button(self):
        button = self.page.button_color_changing()
        assert button.is_displayed()

    def test_appeared_button(self):
        button = self.page.button_appeared()
        assert button.is_displayed()
