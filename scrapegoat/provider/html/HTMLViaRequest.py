import requests
from scrapegoat.models.ScrapConfig import RequestConfig


class HTMLViaRequest:
    def __init__(self, config: RequestConfig):
        self.config = config

    def execute(self) -> requests.Response:
        return requests.request(**self.config.dict())

