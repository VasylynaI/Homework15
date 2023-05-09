from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class RadioButton:
    def __init__(self, driver: WebDriver, locator: tuple):
        self.driver: WebDriver = driver
        self.locator = locator
        self.by, self.loc = locator
        self.locator_name = self.loc + "[contains(@for, '{}')]"
        self.locator_input = "//ancestor::div/input"

    def type_of(self) -> str:
        return self.__class__.__name__

    def select(self, name):
        element = self.driver.find_element(self.by, self.locator_name.format(name))
        element.click()

    def is_selected(self, name: str = None) -> bool:
        element_check_locator = self.locator_name.format(name) + self.locator_input
        element = self.driver.find_element(self.by, element_check_locator)
        return element.is_selected()

    def check_radio_button_text_success_status(self, name):
        element = self.driver.find_element(By.XPATH,
                                           f"//span[@class ='text-success'][text()[contains(., '{name.title()}')]]")
        return element.is_displayed()

    def enable_radio_button(self, name):
        enable_element_locator = self.locator_name.format(name) + self.locator_input
        element = self.driver.find_element(self.by, enable_element_locator)
        if not element.is_enabled():
            self.driver.execute_script("arguments[0].disabled = false;", element)
        return self

    def collect_buttons(self):
        loc = '//input[@type="radio"]'
        collected_buttons = self.driver.find_elements(self.by, loc)
        collected_buttons_info = {}
        for elem in collected_buttons:
            name: str = elem.get_attribute("id")[
                        :-5]
            is_selected = elem.is_selected()
            is_enabled = elem.is_enabled()
            collected_buttons_info.update(
                {name: {'is activated': is_enabled, 'is selected': is_selected}})

        return collected_buttons_info
