#Holds all the functions to calculate if a person drops out of a line or not

#BREAKDOWN
#For a given individual calculate the probability they dropout at this moment given the number of items infront of them
#And their current wait time

#INSTRUCTIONS FOR GERARD

#GIVEN A CUSTOMERS ENTER TIME, THE CURRENT TIME (FLOATS) AND THE NUMBER OF ITEMS INFRONT OF THEM GET THE PROBABILITY THEY DROPOUT
#HAVE A FUNCTION RANDOMLY CHOOSE IF THEY DROPOUT BASED ON THE PROBABILITY, RANDOM SAMPLING

import helpers as hlp
from datetime import datetime
import numpy as np

#Returns the current arrival rate of a queue
def dropout(queue):
    service_time_end = queue[2]
    drop_out_list = queue[3]
    arrival_time = queue[0]
    items = queue[4]
    wait_time = queue[6]
    item_ranges = []
    #wait_time_ranges is a two dimentional array where each index holds an array containing the wait time of persons where the total number of items in front of them fall within the given ranges.
    wait_time_ranges = []
    average_wait_time = []
    for i in range(len(hlp.itemRange)):
        item_ranges.append(0)
        wait_time_ranges.append([])
        average_wait_time.append(0)
    for i in range(len(drop_out_list)):
        #The current_total_items variable holds the total number of items of the person in front of the current peron we are on in the queue.
        current_total_items = 0
        if drop_out_list[i] != '0':
            entered_time = datetime.strptime(arrival_time[i], '%H:%M:%S')#we get the time entered of the person who has dropped out
            time_to_compare = datetime.now()
            j = i - 1
            while j > 0:
                if service_time_end[j] == '0':
                    time_to_compare = datetime.strptime(drop_out_list[j], '%H:%M:%S')
                else:
                    time_to_compare = datetime.strptime(service_time_end[j], '%H:%M:%S')
                
                if time_to_compare.time() > entered_time.time():
                    current_total_items += items[j]
                j -= 1
            for k in range(len(hlp.itemRange)):
                if current_total_items >= hlp.itemRange[k][0] and current_total_items <= hlp.itemRange[k][1]:
                    item_ranges[k] += 1
                    wait_time_ranges[k].append(wait_time[i])
    for i in range(len(hlp.itemRange)):
        if len(wait_time_ranges[i]) > 0:
            average_wait_time[i] = np.mean(wait_time_ranges[i])
        else:
            average_wait_time[i] = 0
    return average_wait_time


def main():
	Queues=hlp.getData()
	for queue in Queues:
		print(queue)
		print("Droput")
		print(dropout(Queues[queue]))
		print("")
 
if __name__=="__main__":
	main()