import pprint
import pymongo
from pymongo import MongoClient

client = MongoClient()
db = client.test_database
posts = db.posts
print posts.count()