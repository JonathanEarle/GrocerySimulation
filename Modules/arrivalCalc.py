#Holds all the functions to calculate the arrival time of a queue

#BREAKDOWN
#Calculates the rate of arrival based on the number of items in a line
#Look at arrival rate of line while there are different ranges of items in the line

#KERSCHEL'S INSTRUCTIONS

#FUNCTION #1
#GIVEN A QUEUE FROM THE DATA COLLECTED LOOK AT ALL THE RANGES OF ITEMS

#FOR EACH RANGE CALCULATE THE ARRIVAL RATE

#RETURN AN ARRAY WITH THE ARRIVAL RATES

#FUNCTION #2
#GIVEN AN ARRAY OF POSSIBLE ARRIVAL RATES OF A QUEUE BASED ON NUMBER OF ITEMS IN THE QUEUE (CALCULATED BEFORE)
#AND THE LIST REPRESENTING THE SIMULATED QUEUE AT A GIVEN TIME

#DETERMINE THE NUMBER OF ITEMS IN THE CURRENT SIMULATION QUEUE (GIVEN^^^) 

#DETERMINE THE ARRIVAL RATE USING THE GIVEN ARRIVAL RATE QUEUE AND THE RECENTLY CALCULATED NUMBER OF ITEMS

#RETURN THE APPROPRIATE ARRIVAL RATE

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