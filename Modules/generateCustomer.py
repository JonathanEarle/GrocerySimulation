#Holds all the functions to generate a customer
import helpers as hlp

#Returns the current arrival rate of a queue
def genCustomer(queue):
	return True

def main():
	Queues=hlp.getData()
	for queue in Queues:
		print(queue)
		print("Customer")
		print(genCustomer(Queues[queue]))
		print("")
 
if __name__=="__main__":
	main()