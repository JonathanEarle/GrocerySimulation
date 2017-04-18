#Simulates multiple queues in a grocery and returns their value based on a value function
import numpy as np 
from Modules import helpers as hlp
from Modules import generateCustomer as cust
from Modules import arrivalCalc as arrRate
from Modules import serviceCalc as serRate
from Modules import dropoutCalc as drop
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
	length=[] #Gets the length of the queue each time someone is removed
	sold=0 #Number of items sold
	elapsed=0
	dropouts=0
	customerCount=0
	
	#Queue Parameters
	card = QueueData[5] 
	waiting = QueueData[7]

	arrRates=arrRate.rateItems(QueueData) #List of possible arrival rates based on the number of items in the queue
	itemAvg = serRate.itemAverage(QueueData) #Average number of items in the queue
	cardOrCash = hlp.TimeDifference(QueueData) #Service time difference between using card and cash
	avgServiceRate = hlp.getServiceRate(QueueData) #The average service rate of the queue
	dropProbs=drop.get_dropout_probability_ranges(QueueData) #Get the probaility of dropout given a number of items in the queue

	servRateCard = serRate.serviceRateCard(card,waiting,cardOrCash)
	servRateCash = serRate.serviceRateCard(card,waiting,cardOrCash)

	#Stores time of the next arrival and time the next person finishes being served
	events={'arrival':0,'service':0} 

	while True:
		#Get the first event to occur between an arrival and a service
		event=min(events, key=events.get)

		#Remove customers which have dropped out of the queue
		numItems=hlp.numItems(queue)
		for i in range(len(queue)-1,-1,-1):
			numItems-=queue[i]['items']
			if(drop.bernoulli_drop_out(dropProbs,numItems)):
				del queue[i]
				dropouts+=1

				if(len(queue)==0): #If dropout makes the queue empty wait for arrival
					event='arrival'

				#Remove one person from the queue for dropout,the closer customer is to the cashier the less likely they are to dropout
				break 

		elapsed=events[event]

		#Ensure we stay within duration limit
		if elapsed>duration:
			break

		if event=='arrival':
			customer=cust.genCustomer(QueueData)
			customer['enterTime']=elapsed
			queue.append(customer)

			arrivalRate=arrRate.genArrivalRate(arrRates,queue)
			events['arrival']+=randExp(arrivalRate) #Get time next person enters the queue

			customerCount+=1

		elif event=='service':
			length.append(len(queue))
			customer=queue.pop(0)
			waitTime.append(elapsed-customer['enterTime'])
			sold+=customer['items']

			#Get time current person finishes being served
			if customer['card'] == 0:
				service=randExp(servRateCash)
			else:
				service=randExp(servRateCard)
			serveTime.append(service)

			if len(queue)>0:
				events['service']+=service
			else:
				#Case of queue restarting, use last arrival time as base for next service time as arrival=service start in empty queue
				events['service']=events['arrival']+service

	probDrop=dropouts/customerCount #Calculate the probability of dropout from the simulation
	return np.mean(waitTime),np.mean(serveTime),np.mean(length),sold,probDrop

#Run a monte carlo simulation on a queue
def monteCarlo(queue,runs=1000): 
    waitTime=[] #Average wait time of each run of the queue
    itemsSold=[] #Number of items sold in duration
    serveTime=[]
    probDrop=[]
    length=[]

    for run in range(runs):
    	wait,service,leng,sold,drops=simulateQueue(queue)
        waitTime.append(wait)
        itemsSold.append(sold)
        serveTime.append(service)
        probDrop.append(drops)
        length.append(leng)

    serviceCost=getServiceCost(serveTime)
    waitCost=getWaitingCost(probDrop,waitTime)

    return np.mean(waitTime),np.mean(serveTime),np.mean(length),np.mean(itemsSold),serviceCost, waitCost

def main():
	Queues=hlp.getData()
	for queue in Queues:
		print(queue)
		print("Expected Wait Time, Expected Service Time,Expected Length, Expected Sales, Cost of Service, Cost of Waiting")
		print(monteCarlo(Queues[queue]))
		print("")

if __name__=="__main__":
	main()