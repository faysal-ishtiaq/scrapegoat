import requests
from selenium import webdriver

from scrapegoat.config import selenium as selenium_config
from scrapegoat.models.ScrapConfig import RequestConfig


class HTMLViaSelenium:
    def __init__(self, config: RequestConfig):
        self.driver = webdriver.Chrome(executable_path=selenium_config.DRIVER_PATH)
        self.config = config

    def execute(self):
        return self.driver.get(self.config.url)

