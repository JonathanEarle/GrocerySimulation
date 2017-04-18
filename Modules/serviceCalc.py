#Holds all the functions to calculate the service rate of an individual

#BREAKDOWN
#Given a customer find the time they take to service by taking the time to cashier their # items plus if any extra time
#is taken by using a card or not

#INSTRUCTIONS
#BASED ON THE NUMBER OF ITEMS A CUSTOMER HAS GET A SERVICE RATE
#EDIT THAT SERVICE RATE BASED ON IF THEY USE A CARD OR NOT 

#GIVEN A CUSTOMER CALCULATE THEIR SERVICE RATE BASED ON THE NUMBER OF ITEMS THEY HAVE AND IF THEY USE A CARD OR NOT

import helpers as hlp
import numpy as np

# returns time to cash 1 item
def perItem(queue):
	items = queue[4]
	start = queue[1][0]
	end = queue[2][len(queue[0])-1]
	return hlp.getElapsed(start,end)/sum(items)

def getRange(itemNum):
	for j in range(len(hlp.itemRange)):
		if itemNum >= hlp.itemRange[j][0] and itemNum <= hlp.itemRange[j][1]:
			return j
	return -1

def itemAverage(queue): 
	items = queue[4]
	total = []
	count = []
	avg = []

	for i in range(len(hlp.itemRange)):
		total.append(0)
		count.append(0)

	for i in range(len(items)):
		itemRang = getRange(items[i])
		
		if itemRang != -1:
			total[itemRang] +=items[i]
			count[itemRang] += 1

	for i in range(len(hlp.itemRange)):
		if count[i] == 0:
			avg.append(0)
		else:
			avg.append(total[i] / float(count[i]))
	return avg

def getRangedServiceRate(queue):
	time = queue[7]
	items = queue[4]
	itemTime = [] #holds times for items within the specified range
	serviceRange = []

	for i in range(len(hlp.itemRange)):
		itemTime.append([])

	for i in range(len(time)):
		itemRang = getRange(items[i])
		if itemRang != -1:
			itemTime[itemRang].append(time[i])

	for i in range(len(hlp.itemRange)):
		if not itemTime[i]:
			serviceRange.append(0)
		else:
			serviceRange.append( 1 / np.mean(itemTime[i]) / 60)
	
	return serviceRange

#Returns the current arrival rate of a queue
def getServiceRate(itemAvg,cardOrCashLiabil,servRate,customer):
	paytime = 0
	itemNum = customer['items']

	itemRang = getRange(itemNum)
	rate = servRate[itemRang]
	avg = float(itemAvg[itemRang])

	ratePerItem = rate / avg
	paytime = cardOrCashLiabil[0]
	
	return (ratePerItem * itemNum) + paytime 

def main():
	Queues=hlp.getData()
	for queue in Queues:
		print(queue)
		print("Service Rate")

		cust = {'items':10,'card':0} #generate customer here

		itemAvg = itemAverage(Queues[queue]) #gets average number of items for items within the range of the customer's items bought
		cardOrCashLiabil = hlp.TimeDifference(Queues[queue])
		servRate = getRangedServiceRate(Queues[queue]) #hlp.getServiceRate(Queues[queue])

		print(getServiceRate(itemAvg,cardOrCashLiabil,servRate,cust))
		print("")
 
if __name__=="__main__":
	main()
