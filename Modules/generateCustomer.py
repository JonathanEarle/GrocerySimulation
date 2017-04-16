#Holds all the functions to generate a customer

#Create a customer dictionary {items,card,enter time} only num items and if they use a card are generated
import helpers as hlp
import numpy as np
import random

itemRange = hlp.itemRange

def sampleItems(prob):
	graph = np.cumsum(prob)
	u = np.random.uniform(0,1)
	num = -1

	for i in range(len(graph)):
		if u <= graph[i]:
			num = i
			break

	for j in range(len(itemRange)):
		if num == j:
			num = random.randrange(itemRange[j][0],itemRange[j][1])
			#break

	return num

#Determines if a person uses a card or not
def cardProb(queue):
	card = queue[5]
	zero = 0
	one = 1
	for i in card:
		if i == '0':
			zero +=1
		else:
			one +=1 
	total = zero + one
	prob = {0:round((zero/float(total)),2),1:round((one/float(total)),2)}

	return prob

# A person comes into the system and it returns the whether they use card (1) or cash (0)
def bernoulliCard(queue):
	sample = np.random.uniform(0,1)
	card = cardProb(queue)
	if sample <= card[0]:
		return 0
	return 1

# Generates a customer with item card and enter time
def genCustomer(queue):
	card = bernoulliCard(queue)
	items = sampleItems(queue[4])
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