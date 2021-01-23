import os
from pymongo import MongoClient


class MongoDBDataStore:
    def __init__(self, collection):
        self.client = MongoClient(host=os.getenv("mongodb_host"), port=os.getenv("mongodb_port", ""))
        self.collection = self.client[os.getenv("mongodb_database")][collection]

    def write(self, document: dict):
        return self.collection.insert_one(document)

    def write_multiple(self, documents: list):
        return self.collection.insert_many(documents)

