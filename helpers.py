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

def getArrivalRate(queue):
	arrivals=queue[0]
	arrivalRates=[]
	for i in range(1,len(arrivals)):
		arrivalRates.append(getElapsed(arrivals[i-1],arrivals[i]))
	return 1/(np.mean(arrivalRates)/60)

def getServiceRate(queue):
	time=queue[7]
	return 1/(np.mean(time)/60)

def getWaitTime(queue):
	time=queue[6]
	return np.mean(time)/60

def getServiceUtil(arrival,service):
	return arrival/service

def getLength(queue):
    stat = 0
    save = 0
    arrival=queue[0]
    s_start=queue[1]
    y = 0
    i = 0
    count = 1 #start at 1 due to for loop starting from index 1
    quesize = [count]
    for i in range(1,len(arrival)):
        skip = 0
        while s_start[y] == 0: #skip to next y if drop out is 0
            y+=1
        if s_start[i]==0: #minus from queue if drop out
            count-=1
        else:
            if arrival[i] > s_start[y]:
                if(stat==0):
                    save =i
                stat=1
                while s_start[y+skip+1]!=0 and s_start[y] > s_start[y+skip+1]: 
                    skip+=1

                count-=skip
                if skip==0:
                    y+=1
                else:
                    y+=skip
            else:
                count+=1
        quesize.append(count)
    return save,quesize


def main():
	getData()
	for queue in Queues:
		print queue

		arr=getArrivalRate(Queues[queue])
		ser=getServiceRate(Queues[queue])
		wait=getWaitTime(Queues[queue])
		length = getLength(Queues[queue])

		print "Length of Queue " ,length
		print "Arrival Rate " ,arr
		print "Service Rate " ,ser
		print "Wait Time " ,wait
		print "Service Utilization " ,getServiceUtil(arr,ser)
		print "\n"

if __name__=="__main__":
	main()