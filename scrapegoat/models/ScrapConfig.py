from typing import Any, List
from pydantic import BaseModel, HttpUrl


class RequestConfig(BaseModel):
    method: str
    url: HttpUrl
    params: dict = None  # sent in query string
    data: dict = None  # sent in request body
    headers: dict = None
    cookies: dict = None
    files: dict = None
    auth: tuple = None
    timeout: float = None
    allow_redirects: bool = True
    proxies: dict = None
    verify: Any = True
    stream: bool = False
    cert: Any = None


class DataMapper(BaseModel):
    selector: str
    name: str
    attribute: str


class ScrapConfiguration(BaseModel):
    """
    When passing scrap configuration along with URL,
    the configuration instance should be validated against this model.
    """
    request_config: RequestConfig
    data_mapper: List[DataMapper]

