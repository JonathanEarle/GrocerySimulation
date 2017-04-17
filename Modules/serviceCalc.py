#Holds all the functions to calculate the service rate of an individual

#BREAKDOWN
#Given a customer find the time they take to service by taking the time to cashier their # items plus if any extra time
#is taken by using a card or not

#INSTRUCTIONS
#BASED ON THE NUMBER OF ITEMS A CUSTOMER HAS GET A SERVICE RATE
#EDIT THAT SERVICE RATE BASED ON IF THEY USE A CARD OR NOT 

#GIVEN A CUSTOMER CALCULATE THEIR SERVICE RATE BASED ON THE NUMBER OF ITEMS THEY HAVE AND IF THEY USE A CARD OR NOT

import helpers as hlp


def itemAverage(queue):
	items = queue[4]
	total = 0
	count = 0

	for i in range(len(items)):
		if items[i] != 0:
			total +=items[i]
			count += 1

	return total / float(count)


#Returns the current arrival rate of a queue
def genServiceRate(queue,customer):
	servRate = hlp.getServiceRate(queue)
	itemAvg = itemAverage(queue)
	paytime = 0
	itemNum = customer['items']

	ratePerItem = servRate / float(itemAvg)

	cardOrCashLiabil = hlp.TimeDifference(queue)

	paytime = cardOrCashLiabil[0]
	
	return (ratePerItem * itemNum) + paytime 

def main():
	Queues=hlp.getData()
	for queue in Queues:
		print(queue)
		print("Service Rate")
		cust = {10,0,0} #generate customer here
		print(genServiceRate(Queues[queue],cust))
		print("")
 
if __name__=="__main__":
	main()
