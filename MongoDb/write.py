import pymongo
import datetime
from pymongo import MongoClient


client = MongoClient()
db = client.test_database

new_posts = [{'author':'Mike'}, {'author':'Richard'}]
posts = db.posts
result = posts.insert_many(new_posts)
result.inserted_ids