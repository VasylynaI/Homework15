import time

from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


def appeared_element(driver: WebDriver, locator: tuple, timeout: int, poll: float | int = 0.2) -> WebElement:
    """
        :param driver: WebDriver
        :param timeout: Max time to wait for element to be enabled
        :param locator: tuple with By. Example: (By.XPATH, "//div[@id]")
        :param poll: Time to sleep in loop
        :return: WebElement if it presents in DOM tree
        """
    end_time = time.monotonic() + timeout
    while time.monotonic() <= end_time:
        try:
            element = driver.find_element(*locator)
            return element
        except NoSuchElementException:
            time.sleep(poll)
            continue
    raise NoSuchElementException(f"Element not found: {locator}")


def enabled_element(driver: WebDriver, locator: tuple, timeout: int) -> WebElement:
    """
       :param driver: WebDriver
       :param locator: tuple with By. Example: (By.XPATH, "//div[@id]")
       :param timeout: Max time to wait for element to be enabled
       :return: WebElement if it presents in DOM tree
       """
    element = driver.find_element(*locator)
    got_element = WebDriverWait(driver, timeout).until(ec.element_to_be_clickable(element))
    return got_element


def wait_element_to_be_enabled(element: WebElement, timeout: int) -> bool:
    """
    :param element: WebElement from function caller
    :param timeout: Max time to wait for element to be enabled
    :return: True if element is enabled
    """
    end_time = time.monotonic() + timeout
    while time.monotonic() <= end_time:
        if element.is_enabled():
            return True
        else:
            time.sleep(0.1)
    raise TimeoutError(f'Element is not enabled after {timeout} seconds')
