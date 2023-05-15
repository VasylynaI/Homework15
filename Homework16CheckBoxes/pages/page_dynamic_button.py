from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from Homework16CheckBoxes.helper.element_waiting import appeared_element, enabled_element, wait_element_to_be_enabled


class PageDynamic:
    _instance = None
    URL = 'https://demoqa.com/dynamic-properties'

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.enabled_after_button = (By.XPATH, '//*[@id="enableAfter"]')
        self.color_change_button = (By.XPATH, '//*[contains(@class, "danger")]')
        self.visible_after_button = (By.XPATH, '//*[@id="visibleAfter"]')

    def open(self):
        self.driver.get(self.URL)
        return self

    def enable_button_v1(self):
        button = self.driver.find_element(*self.enabled_after_button)
        got_button = wait_element_to_be_enabled(button, 10)
        return got_button

    def enable_button_v2(self):
        button = enabled_element(self.driver, self.enabled_after_button, timeout=10)
        return button

    def color_button(self):
        button = appeared_element(self.driver, self.color_change_button, 10, poll=0.2)
        return button

    def visible_button(self):
        button = appeared_element(self.driver, self.visible_after_button, 10, poll=0.2)
        return button
