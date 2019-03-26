import csv
from datetime import datetime


def main():
	user = ""

	with open('text21.csv') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		
		for row in csv_reader:
			#print(f'\t{row[0]} {row[1]} {row[2]} {row[3]}')
			if row[1] != user:
				user = row[1]
				print(f'new user: {row[1]}')
			else:
				time_find()
				
def time_find():
	s1 = '14:51:24'
	s2 = '14:51:44'
	FMT = '%H:%M:%S'
	tdelta = datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)
	print(tdelta)

main()