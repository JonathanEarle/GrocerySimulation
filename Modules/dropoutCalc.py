#Holds all the functions to calculate if a person drops out of a line or not
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