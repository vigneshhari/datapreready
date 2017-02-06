from sklearn.ensemble import RandomForestClassifier
import csv
import numpy as np

# this wont work .. download the csv file .. wait njan thanne downloadam
x = []
y = []

with open("data.csv") as f:
	data = csv.reader(f , delimiter = ",")
	data =  list(data)
	lat_index =  data[0].index('latitude')
	log_index =  data[0].index('longitude')
	country_index =  data[0].index('country_name')

	for row in data:
		x.append([row[lat_index] , row[log_index]]);
		y.append(row[country_index])
		
x = x[1:]
y = y[1:]
country =  list(set(y))
y = [country.index(val) for val in y]
print country

# Machine Learning Part - start 
regr = RandomForestClassifier()
regr.fit(x[:9000], y[:9000])
#Machine Learning Part End 

print country[regr.predict([25.248141 , 51.554443 ])]
print country[regr.predict([25.197197 , 55.274376])]
print country[regr.predict([26.066700 , 50.557700])]
print regr.score(x[9000:],y[9000:]) * 100  , "  Percentage Accuracy"

