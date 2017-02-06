import csv
import pymongo
import datetime
import pprint
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient()
db = client.csv_mongodb
infos = db.infos

def classify_list():
    with open('data.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        readCSV = list(readCSV)
        headings = readCSV[0]
        datas = readCSV[1:]
    l = []
    for index, data in enumerate(datas):
        l.append(data)
    return l

def insert():
    with open('data.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        readCSV = list(readCSV)
        headings = readCSV[0]
        datas = readCSV[1:]
    #print headings
    #print datas[0]
    #The heading contains a list with all the heading and data is a list of data .. each item in the array contains all the data of that particular index in the prescribed format
    l = []
    for index, data in enumerate(datas):
        l.append(zip(headings,data))
    
    print "Current insertion : ", len(l)
    infos.insert_many(l)
    print "Total insertion in db : ", infos.count()

def read():
    for info in infos.find():
        pprint.pprint(info)
    print "Total read : ", infos.count()
    
def delete(item):
    result = infos.delete_one(item)   
    if(result.deleted_count == 1):
        print "Successfully deleted"
    else:
        print "Unsuccessful"
    
def drop():
    print infos.drop()
    
def count():
    print infos.count()
    
def find(item):
    infos.find_one(item)
    print infos.find_one(item)
    
#insert()
#read()
#delete({'_id': ObjectId('5894a0120dc540eb512ef9c4')})
#find({'_id': ObjectId('5894a1b10dc540ff8d5dbb98')})
#drop()
#count()

#classify = classify_list()
#print classify[:6]