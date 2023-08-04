from pymongo import MongoClient
from data import config

async def login(collection_name):
    client = MongoClient(config.MONGOSH_TOKEN)
    db = client[config.MONGOSH_DBASE]
    collection = db[collection_name]
    return collection