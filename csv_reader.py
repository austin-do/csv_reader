import csv
from datetime import datetime

def main():
	users = split_users()
	time_find()
	for row in users[0]:
		print(row[1])

#Puts users into 2 dimensional array with all 1st user log data at arr[0]
def split_users():
	user = ""
	users = []
	count = -1
	
	with open('text21.csv') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		
		for row in csv_reader:
			if row[1] != user:
				users.append([])
				user = row[1]
				count +=1
				users[count].append(row)
			else:
				users[count].append(row)
	return users

#Subtracts and returns two time stamps
def time_find():
	s1 = '14:51:24'
	s2 = '14:51:44'
	FMT = '%H:%M:%S'
	tdelta = datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)
	return(tdelta)

main()