from bs4 import BeautifulSoup
from scrapegoat.models.ScrapConfig import ScrapConfiguration
from scrapegoat.models.ScrapedData import ScrapedData
from scrapegoat.provider.html.HTMLViaRequest import HTMLViaRequest


def scrap(config: ScrapConfiguration) -> ScrapedData:
    response = HTMLViaRequest(config.request_config).execute()
    soup = BeautifulSoup(response.text, "html.parser")
    return ScrapedData(
        config=config,
        data=[
            {
                "value": [
                    getattr(item, mapper.attribute) if mapper.attribute in {
                        "text",
                        "name",
                        "children",
                        "parents",
                        "parent",
                        "attrs"
                    } else item.get(mapper.attribute)
                    for item in soup.select(mapper.selector)
                ],
                **mapper.dict()
            } for mapper in config.data_mapper
        ]
    )
