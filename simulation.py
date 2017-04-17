#Simulates multiple queues in a grocery and returns their value based on a value function
import numpy as np 
from Modules import helpers as hlp
from Modules import generateCustomer as cust
from Modules import arrivalCalc as arrRate
#from Modules import serviceCalc as serRate
#from Modules import dropoutCalc as drop
np.seterr(all='ignore')

#Gets the cost of service
def getServiceCost(serveTime):
	return np.mean(serveTime)*hlp.cashierFee

#Gets the cost of waiting by multiplying expected waiting cost by the probailty of dropout in a queue
def getWaitingCost(drops, waitTime):
	return np.mean(drops)*np.mean(waitTime)

#Get an exp~ random number based on an average rate
def randExp(rate):
	return -(np.log(1-np.random.uniform(0,1))/rate)

#Simulates a specific queue for a duration in minutes
def simulateQueue(QueueData,duration=30.0):
	queue=[] #Data for each customer
	waitTime=[] #Wait time of each served customer
	serveTime=[] #Service time of each customer
	sold=0 #Number of items sold
	elapsed=0
	dropouts=0
	customerCount=0
	
	#Queue Parameters
	#arrRates=arrRate.rateItems(QueueData) #List of possible arrival rates based on the number of items in the queue
	arrivalRate=hlp.getArrivalRate(QueueData)
	serviceRate=hlp.getServiceRate(QueueData)

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
			customer=cust.genCustomer(QueueData)
			customer['enterTime']=elapsed
			queue.append(customer)

			#arrivalRate=arrRate.genArrivalRate(arrRates,hlp.numItems(queue))
			events['arrival']+=randExp(arrivalRate) #Get time next person enters the queue

			customerCount+=1

		elif event=='service':
			customer=queue.pop(0)
			waitTime.append(elapsed-customer['enterTime'])
			sold+=customer['items']

			#Get time current person finishes being served
			#serviceRate=getServiceRate(customer)
			service=randExp(serviceRate)
			serveTime.append(service)

			if len(queue)>0:
				events['service']+=service
			else:
				#Case of queue restarting, use last arrival time as base for next service time as arrival=service start in empty queue
				events['service']=events['arrival']+service

		#Remove customers which have dropped out of the queue
		'''for i,customer in queue:
			if(dropout(customer,queue,elapsed,QueueData)):
				del queue[i]
				dropouts+=1'''

	probDrop=dropouts/customerCount #Calculate the probability of dropout from the simulation
	return np.mean(waitTime),np.mean(serveTime),sold,probDrop

#Run a monte carlo simulation on a queue
def monteCarlo(queueSimulation,queue,runs=1000): 
    waitTime=[] #Average wait time of each run of the queue
    itemsSold=[] #Number of items sold in duration
    serveTime=[]
    probDrop=[]

    for run in range(runs):
    	wait,service,sold,drops=queueSimulation(queue)
        waitTime.append(wait)
        itemsSold.append(sold)
        serveTime.append(service)
        probDrop.append(drops)

    serviceCost=getServiceCost(serveTime)
    waitCost=getWaitingCost(probDrop,waitTime)

    return np.mean(waitTime),np.mean(serveTime),np.mean(itemsSold),serviceCost, waitCost

def main():
	Queues=hlp.getData()
	for queue in Queues:
		print(queue)
		print("Expected Wait Time, Expected Sevice Time, Expected Sales, Cost of Service, Cost of Waiting")
		print(monteCarlo(simulateQueue,Queues[queue]))
		print("")

if __name__=="__main__":
	main()