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

=======
import numpy as np
import helpers as hlp
rangearr = [[1,9], [10,14], [15,19], [20,30], [31,100]]

#Returns the current arrival rate given the # of items 
def genArrivalRate(queue,items):
	loc = -1
	arrivals=queue[0]
	interArrivalTime=[]
	# puts # of items in range
	for i in rangearr:
		if items >= i[0] and items <= i[1]:
			itemRange = i
	# checks to see if person in is that item range if they are gets their time elasped from last person
	for person in queue[4]:
		loc +=1
		if person >= itemRange[0] and person <= itemRange[1]:
			interArrivalTime.append(hlp.getElapsed(arrivals[loc-1],arrivals[loc]))
	# Express lines can only have 1-10 so it returns nan for other values
	if interArrivalTime:
		return abs(1/(np.mean(interArrivalTime)/60))

	

def main():
	Queues=hlp.getData()
	for queue in Queues:
		print(queue)
		print("Arrival Rate")
		print(genArrivalRate(Queues[queue],31))
		print("")
 
if __name__=="__main__":
	main()