import csv
with open('data.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    readCSV = list(readCSV)
    heading = readCSV[0]
    data = readCSV[1:]
print heading
print data[0]
// the heading contains a list with all the heading and data is a list of data .. each item in the array contains all the data of that particular index in the prescribed format