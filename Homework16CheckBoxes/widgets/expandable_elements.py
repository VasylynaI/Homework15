from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException


class ExpandableTreeElement:
    def __init__(self, driver: WebDriver, locator: tuple):
        self.driver: WebDriver = driver
        self.locator = locator
        self.by, self.loc = locator
        self.expand_loc_name = self.loc + "[contains(@for, '{}')]//ancestor::span/button"
        self.folder_selection_state_loc_name = self.loc + "[contains(@for, '{}')]"
        self.folder_selection_state_loc_name_input = self.loc + "[contains(@for, '{}')]/input"

    def __change_folder_expand_state(self, name: str, expand_action: bool):
        loc_name = self.expand_loc_name.format(name)
        element = self.driver.find_element(self.by, loc_name)
        try:
            if expand_action:
                expand = element.find_element(By.XPATH, '//*[contains(@class, "expand-close")]')
                if expand.is_displayed():
                    element.click()
            else:
                collapse = element.find_element(By.XPATH, '//*[contains(@class, "expand-open")]')
                if collapse.is_displayed():
                    element.click()
        except NoSuchElementException:
            pass

    def expand_folder(self, name) -> None:
        self.__change_folder_expand_state(name=name, expand_action=True)

    def collapse_folder(self, name) -> None:
        self.__change_folder_expand_state(name=name, expand_action=False)

    def __change_folder_selection_state(self, name, enabled=False):
        loc_name = self.folder_selection_state_loc_name.format(name)
        loc_name_input = self.folder_selection_state_loc_name_input.format(name)
        element = self.driver.find_element(self.by, loc_name)
        element_input = self.driver.find_element(self.by, loc_name_input)
        if enabled:
            if not element_input.is_selected():
                element.click()
        else:
            if element_input.is_selected():
                element.click()

    def mark_folder(self, name):
        self.__change_folder_selection_state(name, enabled=True)

    def unmark_folder(self, name):
        self.__change_folder_selection_state(name, enabled=False)
