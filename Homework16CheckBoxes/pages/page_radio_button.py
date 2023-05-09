from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from Homework16CheckBoxes.widgets.radio_button import RadioButton


class PageRadioButton:
    _instance = None
    URL = "https://demoqa.com/radio-button"

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver
        self.page_radio_button = RadioButton(self.driver, (By.XPATH, '//label[contains(@for, "Radio")]'))

    def open(self):
        self.driver.get(self.URL)
        return self

    def select_radio_button(self, name):
        self.page_radio_button.select(name)

    def is_selected_radio_button(self, name):
        return self.page_radio_button.is_selected(name)

    def check_radio_button_text_status(self, name):
        return self.page_radio_button.check_radio_button_text_success_status(name)

    def enable_radio_button(self, name):
        return self.page_radio_button.enable_radio_button(name)

    def collect_buttons_info(self):
        return self.page_radio_button.collect_buttons()
