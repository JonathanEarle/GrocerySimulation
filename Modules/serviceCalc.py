#Holds all the functions to calculate the service rate of an individual
import helpers as hlp

#Returns the current arrival rate of a queue
def genServiceRate(queue):
	return True

def main():
	Queues=hlp.getData()
	for queue in Queues:
		print(queue)
		print("Service Rate")
		print(genServiceRate(Queues[queue]))
		print("")
 
if __name__=="__main__":
	main()