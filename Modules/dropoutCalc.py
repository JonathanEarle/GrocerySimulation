#Holds all the functions to calculate if a person drops out of a line or not

#BREAKDOWN
#For a given individual calculate the probability they dropout at this moment given the number of items infront of them
#And their current wait time

import helpers as hlp

#Returns the current arrival rate of a queue
def dropout(queue):
	return True

def main():
	Queues=hlp.getData()
	for queue in Queues:
		print(queue)
		print("Droput")
		print(dropout(Queues[queue]))
		print("")
 
if __name__=="__main__":
	main()