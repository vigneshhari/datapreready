import cPickle as pickle
import pymongo
from pymongo import MongoClient

client = MongoClient()
db = client.csv_mongodb
infos = db.infos

x_val = ['latitude','longitude']
y_val = 'country_name'
temp= []
finalx = []
finaly = []



xunf = {}
for i in x_val:
	xunf[i] = []


for info in infos.find():
	print len(finaly)
	finaly.append(info[y_val].encode('utf8'))
	looper= 0
	for i in x_val:
		try:
			print looper
			xunf[i].append(float(info[i].encode('utf8')))
		except Exception as e :
			print e
			xunf[i].append(info[i].encode('utf8'))
	#print 'info:',infos.count()
print "latitude" , len(xunf['latitude'])
print "longitude" , len(xunf['longitude'])
print xunf['longitude'][0] , " and " , xunf['latitude'][0]

'''
for info in infos.find():
    for x in x_val:
        temp.append(info[x].encode('utf8'))
    finaly.append(info[y_val].encode('utf8'))
    finalx.append(temp)
    temp = []
'''


for i in finaly:
	try:
		pp =  float(i)
	except:
		keys =  list(set(finaly))
		finaly = [keys.index(val) for val in finaly]
		break


for x in xunf.keys():
	for i in xunf[x]: 
		try:
			pp =  float(i)
		except:
			keys =  list(set(xunf[x]))
			temp = [keys.index(val) for val in xunf[x]]
			xunf[x] = temp
			break
finalx = []


for i in range(0,len(xunf.values()[0])):
	temp = []
	for k in xunf.values():
		temp.append(k[i])
	finalx.append(temp)


