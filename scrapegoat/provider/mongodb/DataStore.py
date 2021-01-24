import os
from pymongo import MongoClient
from scrapegoat.config import mongodb


class MongoDBDataStore:
    def __init__(self, collection):
        self.client = MongoClient(host=mongodb.HOST, port=mongodb.PORT)
        self.collection = self.client[mongodb.DB_NAME][collection]

    def write(self, document: dict):
        return self.collection.insert_one(document)

    def write_multiple(self, documents: list):
        return self.collection.insert_many(documents)

