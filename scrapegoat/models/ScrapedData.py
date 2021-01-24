from pydantic import BaseModel
from typing import Any, List
from scrapegoat.models.ScrapConfig import ScrapConfiguration


class ScrapedItem(BaseModel):
    name: str
    selector: str
    value: Any


class ScrapedData(BaseModel):
    config: ScrapConfiguration
    data: List[ScrapedItem]
