import csv
from datetime import datetime
from datetime import timedelta

def main():
	users = split_users()
	find_login_times(users)

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

def find_login_times(users):
	pass_entered = []
	pass_submitted = []
	success_time = 0
	failure_time = 0
	success_count = 0
	failure_count = 0
	
	for row in users[0]:
		if row[5] == "enter":
			pass_entered = pass_submitted
			pass_submitted = row
		if row[5] == "login":
			if row[6] == "success":
				success_count += 1
				success_time = time_find(success_time,pass_entered[0],pass_submitted[0])
			else:
				failure_count += 1
				failure_time = time_find(failure_time,pass_entered[0],pass_submitted[0])
			
	s = success_time/success_count
	f = failure_time/failure_count
	
	returnval = []
	returnval.append(timedelta(seconds = s))
	returnval.append(timedelta(seconds = f))
	
	print(returnval)
	return(returnval)
	
#Subtracts and returns two time stamps
def time_find(total_time, pass_entered, pass_submitted):
	s1 = pass_entered
	s2 = pass_submitted
	FMT = '%Y-%m-%d %H:%M:%S'
	tdelta = datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)
	total_time = total_time + tdelta.total_seconds()
	return(total_time)

main()