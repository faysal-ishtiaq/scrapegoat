from pydantic import BaseModel, Field


class RequestConfig(BaseModel):
    method: str
    timeout: int = None


class ScrapConfiguration(BaseModel):
    """
    When passing scrap configuration along with URL,
    the configuration instance should be validated against this model.
    """
    request_config: RequestConfig
    data_mapper: DataMapper

