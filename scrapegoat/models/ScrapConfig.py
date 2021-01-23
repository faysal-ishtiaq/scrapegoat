from typing import Either
from pydantic import BaseModel, Field


class RequestConfig(BaseModel):
    method: str
    url: str
    params: dict = None  # sent in query string
    data: dict = None  # sent in request body
    json: dict = None  # sent in request body
    headers: dict = None
    cookies: dict = None
    files: dict = None
    auth: tuple = None
    timeout: float = None
    allow_redirects: bool = True
    proxies: dict = None
    verify: bool = True
    stream: bool = False
    cert: str = None


class ScrapConfiguration(BaseModel):
    """
    When passing scrap configuration along with URL,
    the configuration instance should be validated against this model.
    """
    request_config: RequestConfig
    data_mapper: DataMapper

