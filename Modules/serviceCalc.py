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


def itemAverage(queue):
	items = queue[4]
	total = 0
	count = 0

	for i in range(len(items)):
		if items[i] != 0:
			total +=items[i]
			count += 1

	return total / float(count)

# returns time to cash 1 item
def perItem(queue):
	items = queue[4]
	start = queue[1][0]
	end = queue[2][len(queue[0])-1]
	return hlp.getElapsed(start,end)/sum(items)
	

# Service rate based on if used cash
def serviceRateCash(card,time,cardOrCashLiabil):
	cash = []
	for i in range(len(time)-1):
		if card[i] == '0':
			time [i] = time[i]+cardOrCashLiabil[0]
			cash.append(time[i])
	return 1/(np.mean(cash)/60)

# Service rate based on if used card

def serviceRateCard(card,time,cardOrCashLiabil):
	cash = []
	for i in range(len(time)-1):
		if card[i] == '1':
			val = time[i]+cardOrCashLiabil[1]
			cash.append(val)
	return 1/(np.mean(cash)/60)


def main():
	Queues=hlp.getData()
	for queue in Queues:
		print(queue)
		print("Service Rate")
		cardOrCashLiabil = hlp.TimeDifference(Queues[queue])
		print serviceRateCard(Queues[queue][5],Queues[queue][7],cardOrCashLiabil)

if __name__=="__main__":
	main()
