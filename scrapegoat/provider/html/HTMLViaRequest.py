import requests


class HTMLViaRequest:
    def __init__(self, url: str, method: str, params: dict = None):
        self.url = url
        self.method = method
        self.params = params

    def make_request(self):
        requester = None
        if self.method.lower() == "get":
            requester = requests.get
        if self.method.lower() == "post":
            requester = requests.post

        return requester(self.url, **self.params)

    def get_html(self):
        response = self.make_request()
        return response.text
