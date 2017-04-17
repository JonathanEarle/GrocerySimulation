#Holds all the functions to calculate the service rate of an individual

#BREAKDOWN
#Given a customer find the time they take to service by taking the time to cashier their # items plus if any extra time
#is taken by using a card or not

#INSTRUCTIONS
#BASED ON THE NUMBER OF ITEMS A CUSTOMER HAS GET A SERVICE RATE
#EDIT THAT SERVICE RATE BASED ON IF THEY USE A CARD OR NOT 

#GIVEN A CUSTOMER CALCULATE THEIR SERVICE RATE BASED ON THE NUMBER OF ITEMS THEY HAVE AND IF THEY USE A CARD OR NOT

import helpers as hlp

def getCardValue(queue):
	cardOrCash = queue[5]
	servTime = queue[7]
	items = queue[4]
	cardTotal = 0 #gets total service time for card users
	cardCount = 0
	cardItems = 0 #gets number of items for card users
	cashTotal = 0
	cashCount = 0
	cashItems = 0

	for i in range(len(servTime)):
		if servTime[i]!= 0:
			if cardOrCash == 0:#cash
				cashTotal += servTime[i]
				cashCount += 1
				cashItems += items[i]
			else: #card
				cardTotal += servTime[i]
				cardCount += 1
				cardItems += items[i]

	if cashCount == 0:
		cashAvg = 0
	else:
		cashAvg = cashTotal / float(cashCount) #gets average service time for cash users

	if cardCount == 0:
		cardAvg = 0
	else:
		cardAvg = cardTotal / float(cardCount)

	cashAvg = cashAvg / float(cashItems) #gets average per item
	cardAvg = cardAvg / float(cardItems) 

	return cardAvg - cashAvg

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

	cardOrCashLiabil = getCardValue(queue)

	if cardOrCashLiabil > 0 and customer['card'] == 1: #customer used card and using card takes more time
		paytime = cardOrCashLiabil
	elif cardOrCashLiabil < 0 and customer['card'] == 0: #customer used cash and using cash takes more time
		paytime = abs(cardOrCashLiabil)

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