import click

from bs4 import BeautifulSoup

from scrapegoat.config import mongodb as mongodb_config
from scrapegoat.provider.html.HTMLViaRequest import HTMLViaRequest
from scrapegoat.provider.mongodb.DataStore import MongoDBDataStore
from scrapegoat.validator.SchemaValidator import SchemaValidator


@click.group()
def cli():
    pass


@click.command()
@click.argument("url")
@click.argument("config")
def scrape(url, scrap_config):
    datastore = MongoDBDataStore(collection=mongodb_config.DEFAULT_COLLECTION)
    method = scrap_config.pop("method")
    selector_mapping = scrap_config.pop("selector_mapping")
    html_provider = HTMLViaRequest(url=url, method=method, params=scrap_config)
    soup = BeautifulSoup(html_provider.get_html())
    for _selector, _config in selector_mapping.items():
        data_type = _config.pop("data_type")
        attribute = _config.pop("attribute")

        value = [item.get(attribute) for item in soup.select(_selector)]

        if len(value) == 1:
            value = value[0]

        if SchemaValidator.validate(value, data_type):
            # write_data(url, selector, name, value)
            datastore.write(value)


