#Simulates multiple queues in a grocery and returns their value based on a value function
import numpy as np 
from Modules import helpers as hlp

#Computes the value of a queue
def value(items,avgWaitTime,duration):
	return items/(avgWaitTime+(hlp.cashierFee*duration))

#Get an exp~ random number based on an average rate
def randExp(rate):
	return -(np.log(1-np.random.uniform(0,1))/rate)

#Simulates a specific queue for a duration in minutes
def simulateQueue(QueueData,duration=30.0):
	queue=[] #Data for each customer
	waitTime=[] #Wait time of each served customer
	sold=[] #Number of items sold
	elapsed=0
	service=False #Indicates if someone is currently being serviced
	
	#Queue Parameters
	arrivalRate=hlp.getArrivalRate(QueueData)
	serviceRate=hlp.getServiceRate(QueueData)
	#index 0 for wait time for cash and 1 for card
	WaitCashorCard = hlp.TimeDifference(QueueData)
	#Stores time of the next arrival and time the next person finishes being served
	events={'arrival':0,'service':0} 

	while True:
		#Get the first event to occur between an arrival and a service
		event=min(events, key=events.get)
		elapsed=events[event]

		#Ensure we stay within duration limit
		if elapsed>duration:
			break

		if event=='arrival':
			#customer=genCustomer(QueueData)
			items = hlp.sampleItems(QueueData[4])
			cardOrCash = hlp.bernolliCard(QueueData)
			queue.append({'items':items,'card':cardOrCash,'enterTime':elapsed})
			#arrivalRate=getArrivalRate(QueueData)
			events['arrival']+=randExp(arrivalRate) #Get time next person enters the queue

		elif event=='service':
			customer=queue.pop(0)
			# if user uses card or cash it increases or leaves their wait time 
			if customer['card'] == 0:
				waitTime.append((elapsed-customer['enterTime']) + WaitCashorCard[0])
			elif customer['card'] == 1:
				waitTime.append((elapsed-customer['enterTime']) + WaitCashorCard[1])
			sold.append(customer['items'])
			#serviceRate=getServiceRate(customer)
			#Get time current person finishes being served
			if len(queue)>0:
				events['service']+=randExp(serviceRate)
			else:
				#Case of queue restarting, use last arrival time as base for next service time as arrival=service start in empty queue
				events['service']=events['arrival']+randExp(serviceRate)

		#Remove customers which have dropped out of the queue
		'''for i,customer in queue:
			if(dropout(customer, QueueData)):
				del queue[i]'''

	return np.mean(waitTime),np.sum(sold),duration

#Run a monte carlo simulation on a queue
def monteCarlo(queueSimulation,queue,runs=1000): 
    waitTime=[] #Average wait time of each run of the queue
    itemsSold=[] #Number of items sold in duration
    Value=[] #Value of the queue

    for run in range(runs):
    	wait,sold,duration=queueSimulation(queue)
        waitTime.append(wait)
        itemsSold.append(sold)
        Value.append(value(sold,wait,duration))

    return np.mean(waitTime), np.mean(itemsSold),np.mean(Value)

def main():
	Queues=hlp.getData()
	for queue in Queues:
		print(queue)
		print("Expected Wait Time,Expected Items Sold,Value")
		print(monteCarlo(simulateQueue,Queues[queue]))
		print("")

if __name__=="__main__":
	main()