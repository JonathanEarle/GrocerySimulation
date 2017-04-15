#Holds all the functions to calculate the arrival time of a queue

#BREAKDOWN
#Calculates the rate of arrival based on the number of items in a line
#Look at arrival rate of line while there are different ranges of items in the line

import helpers as hlp

#Returns the current arrival rate of a queue
def genArrivalRate(queue):
	return True

def main():
	Queues=hlp.getData()
	for queue in Queues:
		print(queue)
		print("Arrival Rate")
		print(genArrivalRate(Queues[queue]))
		print("")
 
if __name__=="__main__":
	main()