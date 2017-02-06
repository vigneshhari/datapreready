import pprint
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient()
db = client.csv_mongodb
infos = db.infos

for info in infos.find():
    print info['latitude'], info['longitude']