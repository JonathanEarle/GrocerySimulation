#Holds all the functions to generate a customer

#Create a customer dictionary {items,card,enter time} only num items and if they use a card are generated
from random import randrange
import datetime 
import helpers as hlp

# Generates a customer with item card and enter time
def genCustomer(queue):
	arr=hlp.getArrivalRate(queue)
	amt = 30/float(arr)
	startDate = datetime.datetime(2017, 9, 20,13,00)
	card = hlp.bernolliCard(queue)
	items = hlp.sampleItems(queue[4])
	return {'items':items,'card':card}


def main():
	Queues=hlp.getData()
	for queue in Queues:
		print(queue)
		print("Customer")
		print(genCustomer(Queues[queue]))
		print("")
 
if __name__=="__main__":
	main()