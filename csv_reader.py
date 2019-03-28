import csv
from datetime import datetime
from datetime import timedelta

def main():
	text_processor()
	image_processor()

def text_processor():
	users = split_users('text21.csv')
	for user in users:
		find_text_login_times(user)
	
def image_processor():
	users = split_users('imagept21.csv')
	for user in users:
		find_image_login_times(user)
	
#Puts users into 2 dimensional array with all 1st user log data at arr[0]
def split_users(fn):
	user = ""
	users = []
	count = -1
	
	with open(fn) as csv_file:
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

#finds average logins of success/failure for a user (text)
def find_text_login_times(users):
	#trackers
	pass_entered = []
	pass_submitted = []
	success_time = 0
	failure_time = 0
	success_count = 0
	failure_count = 0
	print(users[0][1])
	for row in users:
		if row[5] == "enter":
			pass_entered = pass_submitted
			pass_submitted = row
		if row[5] == "login":
			if row[6] == "success":
				success_count += 1
				success_time = time_find(success_time,pass_entered[0],pass_submitted[0])
			#if it's a failure
			else:
				failure_count += 1
				failure_time = time_find(failure_time,pass_entered[0],pass_submitted[0])
			
	try:		
		s = success_time/success_count
	except:
		s = 0
	try:
		f = failure_time/failure_count
	except:
		f = 0
	
	returnval = []
	returnval.append(success_count + failure_count)
	returnval.append(success_count)
	returnval.append(failure_count)
	returnval.append(str(timedelta(seconds = s)))
	returnval.append(str(timedelta(seconds = f)))
	
	print(returnval)
	return(returnval)

#finds average logins of success/failure for a user (images)
def find_image_login_times(users):
	#trackers
	pass_entered = []
	pass_submitted = []
	good_login = []
	success_time = 0
	failure_time = 0
	success_count = 0
	failure_count = 0
	
	print(users[0][1])
	for row in users:
		if row[5] == "enter":
			pass_entered = pass_submitted
			pass_submitted = good_login
			good_login = row
		if row[5] == "login":
			if row[6] == "success":
				success_count += 1
				success_time = time_find(success_time,pass_entered[0],pass_submitted[0])
			#if it's a failure
			else:
				failure_count += 1
				failure_time = time_find(failure_time,pass_entered[0],pass_submitted[0])
	try:		
		s = success_time/success_count
	except:
		s = 0
	try:
		f = failure_time/failure_count
	except:
		f = 0
	
	returnval = []
	returnval.append(success_count + failure_count)
	returnval.append(success_count)
	returnval.append(failure_count)
	returnval.append(str(timedelta(seconds = s)))
	returnval.append(str(timedelta(seconds = f)))
	
	print(returnval)
	return(returnval)
	
#Subtracts values and then adds to total returns as int. Used in find_login_times()
def time_find(total_time, pass_entered, pass_submitted):
	s1 = pass_entered
	s2 = pass_submitted
	FMT = '%Y-%m-%d %H:%M:%S'
	tdelta = datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)
	total_time = total_time + tdelta.total_seconds()
	return(total_time)

main()