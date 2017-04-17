#Holds all the functions to calculate the service rate of an individual

#BREAKDOWN
#Given a customer find the time they take to service by taking the time to cashier their # items plus if any extra time
#is taken by using a card or not

#INSTRUCTIONS
#BASED ON THE NUMBER OF ITEMS A CUSTOMER HAS GET A SERVICE RATE
#EDIT THAT SERVICE RATE BASED ON IF THEY USE A CARD OR NOT 

#GIVEN A CUSTOMER CALCULATE THEIR SERVICE RATE BASED ON THE NUMBER OF ITEMS THEY HAVE AND IF THEY USE A CARD OR NOT

import helpers as hlp

#Returns the current arrival rate of a queue
def genServiceRate(queue):
	return hlp.getServiceRate(queue)

def main():
	Queues=hlp.getData()
	for queue in Queues:
		print(queue)
		print("Service Rate")
		print(genServiceRate(Queues[queue]))
		print("")
 
if __name__=="__main__":
	main()