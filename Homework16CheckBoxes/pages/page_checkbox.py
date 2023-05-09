from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from Homework16CheckBoxes.widgets.expandable_elements import ExpandableTreeElement


class PageCheckbox:
    _instance = None
    URL = "https://demoqa.com/checkbox"

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver
        self.folder_widget = ExpandableTreeElement(self.driver, (By.XPATH, '//label[contains(@for, "tree-node-")]'))

    def open(self):
        self.driver.get(self.URL)
        return self

    def page_expand_folder(self, name):
        self.folder_widget.expand_folder(name)

    def page_collapse_folder(self, name):
        self.folder_widget.collapse_folder(name)

    def page_mark_folder(self, name):
        self.folder_widget.mark_folder(name)

    def page_unmark_folder(self, name):
        self.folder_widget.mark_folder(name)
