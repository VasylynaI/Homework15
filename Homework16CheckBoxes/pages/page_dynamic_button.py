from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from Homework16CheckBoxes.helper.element_waiting import get_appeared_element, get_enabled_element_v1, get_enabled_element_v2


class PageDynamic:
    _instance = None
    URL = 'https://demoqa.com/dynamic-properties'

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.enabled_disabled_button_loc = (By.XPATH, '//*[@id="enableAfter"]')
        self.color_button_loc = (By.XPATH, '//*[contains(@class, "danger")]')
        self.invisible_visible_button = (By.XPATH, '//*[@id="visibleAfter"]')

    def open(self):
        self.driver.get(self.URL)
        return self

    def button_disabled_enabled_v1(self):
        button = self.driver.find_element(*self.enabled_disabled_button_loc)
        button = get_enabled_element_v2(button, 10)
        return button

    def button_disabled_enabled_v2(self):
        button = get_enabled_element_v1(self.driver, self.enabled_disabled_button_loc, timeout=10)
        return button

    def button_color_changing(self):
        button = get_appeared_element(self.driver, self.color_button_loc, 10, poll=0.2)
        return button

    def button_appeared(self):
        button = get_appeared_element(self.driver, self.invisible_visible_button, 10, poll=0.2)
        return button
