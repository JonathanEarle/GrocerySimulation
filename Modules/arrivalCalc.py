#Holds all the functions to calculate the arrival time of a queue

#BREAKDOWN
#Calculates the rate of arrival based on the number of items in a line
#Look at arrival rate of line while there are different ranges of items in the line


import numpy as np
import helpers as hlp

rangearr = hlp.itemRange
vals = [0,0,0,0,0]
count = [0,0,0,0,0]

#Returns the current array of arrival rates given the # of items ranges from file
def rateItems(queue):
	ranges =[]
	arrivals=queue[0]
	leave = queue[2]
	items = queue[4]
 	interArrivalTime=[]
	# puts # of items in range

	total =0
	loc = -1
	for j in items:
		loc +=1
		if leave[loc-1] > arrivals[loc]:
			total += j
			interArrivalTime.append(abs(hlp.getElapsed(arrivals[loc-1],arrivals[loc])))
		else:
			total = 0
			interArrivalTime=[]

		if interArrivalTime:
			index = -1
			for i in rangearr:
				index +=1
				if total >= i[0] and total <=i[1]:
					ranges.append({str(index):1/(np.mean(interArrivalTime)/60)})		

	for i in ranges:
	 	for key in i:
	 		vals[int(key)] += i[key]
	for i in ranges:
	 	for key in i:
	 		count[int(key)]+=1

	for i in range(len(vals)):
		vals[i] = vals[i]/float(count[i])

	return vals

# Given # of items range it gives the arrival rate
def genArrivalRate(rates,items):
	count =-1
	for i in rangearr:
		count +=1
		if items >= i[0] and items <=i[1]:
			return rates[count]

def main(): 
	items = 30 #30 items infront of customer
	Queues=hlp.getData()
	for queue in Queues:
		print(queue)
		print("Arrival Rate")
		rates = rateItems(Queues[queue])
		print(genArrivalRate(rates,items))
		print("")
 
if __name__=="__main__":
	main()