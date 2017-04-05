import glob, os
import numpy as np
import sys
import csv
from datetime import datetime

Queues={}

def toSeconds(time):
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
				waitTime.append(toSeconds(row[7]))
				serviceTime.append(toSeconds(row[8]))
			Queues[file]=(arrival,serviceStart,servceEnd,droptime,items,card,waitTime,serviceTime)

	return Queues

def getElapsed(time1,time2):
	elapsed = datetime.strptime(time2, '%H:%M:%S') - datetime.strptime(time1, '%H:%M:%S')
	return elapsed.total_seconds()

def getArrivalRate(arrivals):
	arrivals=arrivals[0]
	arrivalRates=[]
	for i in range(1,len(arrivals)):
		arrivalRates.append(getElapsed(arrivals[i-1],arrivals[i]))
	return 1/(np.mean(arrivalRates)/60)

def getServiceRate(time):
	time=time[7]
	return 1/(np.mean(time)/60)

def getWaitTime(time):
	time=time[6]
	return np.mean(time)/60

getData()
for queue in Queues:
	print queue
	print "Arrival Rate " ,getArrivalRate(Queues[queue])
	print "Service Rate " ,getServiceRate(Queues[queue])
	print "Wait Time " ,getWaitTime(Queues[queue])
	print "\n"

