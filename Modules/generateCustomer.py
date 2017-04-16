#Holds all the functions to generate a customer

#Create a customer dictionary {items,card,enter time} only num items and if they use a card are generated
from random import randrange
import datetime 
import helpers as hlp

def random_time(start,ranges):
   current = start
   curr = current + datetime.timedelta(minutes=randrange(int(ranges)))
   yield curr

# Generates a customer with item card and enter time
def genCustomer(queue):
	arr=hlp.getArrivalRate(queue)
	amt = 30/float(arr)
	startDate = datetime.datetime(2017, 9, 20,13,00)
	card = hlp.bernolliCard(queue)
	items = hlp.sampleItems(queue[4])
	# Using the arrival time ratio it determines how many people a min so 60* arr gives the next interval for customer to enter
	for time in random_time(startDate,arr*60):
		enterTime = time.strftime("%H:%M:%S")
	startDate = datetime.datetime(2017, 9, 20,13,int(time.strftime('%M')))
	return {'items':items,'card':card,'arrival':enterTime}


def main():
	Queues=hlp.getData()
	for queue in Queues:
		print(queue)
		print("Customer")
		print(genCustomer(Queues[queue]))
		print("")
 
if __name__=="__main__":
	main()