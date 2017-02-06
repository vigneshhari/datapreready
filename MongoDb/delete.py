import pprint
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient()
db = client.test_database
posts = db.posts
#posts.remove()#one sec da nee chey
result = posts.delete_many({'author':'Richard'})
print result.deleted_count
