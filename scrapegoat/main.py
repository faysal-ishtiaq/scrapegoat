import json
from scrapegoat.commands import scrap
from scrapegoat.models.ScrapConfig import ScrapConfiguration
from scrapegoat.provider.mongodb.DataStore import MongoDBDataStore

if __name__ == '__main__':
    scraped_data = scrap.scrap(ScrapConfiguration(
        **{
            "request_config": {"url": 'https://python.org', "method": "get"},
            "data_mapper": [
                {
                    "selector": "title",
                    "name": "Title",
                    "attribute": "text"
                },
                {
                    "selector": "#content div section div div.small-widget h2",
                    "name": "Widget Title",
                    "attribute": "text"
                }
            ]
        }
    ))

    for item in scraped_data.data:
        data_store = MongoDBDataStore("scraped_data")
        data_store.write({
            "url": scraped_data.config.request_config.url,
            **item.dict()
        })
