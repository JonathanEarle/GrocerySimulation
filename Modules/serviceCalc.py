#Holds all the functions to calculate the service rate of an individual

#BREAKDOWN
#Given a customer find the time they take to service by taking the time to cashier their # items plus if any extra time
#is taken by using a card or not

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