from typing import List

from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver


class Page:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def find_element(self, locator: tuple, multiple: bool = False) -> List | WebElement:
        if multiple:
            return self.driver.find_elements(*locator)
        return self.driver.find_element(*locator)

    @staticmethod
    def click_element(element: WebElement) -> None:
        element.click()

    @staticmethod
    def fill_input_field(element: WebElement, data: str):
        element.send_keys(data)
