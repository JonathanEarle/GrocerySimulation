import glob, os
import sys
import csv

Queues={'Q1':[],'Q2':[],'Q3':[],'Q4':[],'Q5':[],'Exp':[]}

def toMin(time):
	if(time=='0'):
		return 0
	times=time.split(":")
	return (int(times[0])*60)+int(times[1].split(".")[0])

def getData():
	os.chdir("./")
	for file in glob.glob("*.csv"):
		with open(file) as csvfile:
			data=csv.reader(csvfile,delimiter=',')
			next(data, None)
			arrival=[];serviceStart=[];servceEnd=[]
			droptime=[];items=[];card=[]
			waitTime=[];serviceTime=[]
			for row in data:
				arrival.append(row[1])
				serviceStart.append(row[2])
				servceEnd.append(row[3])
				droptime.append(row[4])
				items.append(row[5])
				card.append(row[6])
				waitTime.append(toMin(row[7]))
				serviceTime.append(toMin(row[8]))
			Queues[file]=(arrival,serviceStart,servceEnd,droptime,items,card,waitTime,serviceTime)

	print Queues

getData()