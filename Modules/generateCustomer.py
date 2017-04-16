#Holds all the functions to generate a customer

#Create a customer dictionary {items,card,enter time} only num items and if they use a card are generated
import helpers as hlp

# Generates a customer with item card and enter time
def genCustomer(queue):
	card = hlp.bernolliCard(queue)
	items = hlp.sampleItems(queue[4])
	return {'items':items,'card':card,'arrival':''}


def main():
	Queues=hlp.getData()
	for queue in Queues:
		print(queue)
		print("Customer")
		print(genCustomer(Queues[queue]))
		print("")
 
if __name__=="__main__":
	main()