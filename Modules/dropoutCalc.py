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

#Returns an array in which the values represent the average wait time of persons who dropped out of the queue with total number in front of them within the ranges speicified by the hlp.itemRange array.
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
            #Note that a person is only in front of another in the queue if their service end time(or drop out time) is after the time the current person(i) entered the queue.
            while j > 0:#we use a while loop to trace backward to see who was in the queue at the time the current person(i) was in the queue
                if service_time_end[j] == '0':#If the service end time is 0 meaning the person has dropped out then we use their drop out time to determine if they were in the queue at the time the current person(i) enetered the queue
                    time_to_compare = datetime.strptime(drop_out_list[j], '%H:%M:%S')
                else:
                    time_to_compare = datetime.strptime(service_time_end[j], '%H:%M:%S')
                
                if time_to_compare.time() > entered_time.time():#The person(j) is only in fron of the person(i) if the time person(j) left the queue(either service end time or drop out time) is after the time the time person(i) entered the queue
                    current_total_items += items[j]#we add to the total number of items in front of the current person(i)
                j -= 1
            for k in range(len(hlp.itemRange)):
                if current_total_items >= hlp.itemRange[k][0] and current_total_items <= hlp.itemRange[k][1]:
                    item_ranges[k] += 1
                    wait_time_ranges[k].append(wait_time[i])
    for i in range(len(hlp.itemRange)):
        if len(wait_time_ranges[i]) > 0:
            average_wait_time[i] = np.mean(wait_time_ranges[i])
        else:
            average_wait_time[i] = 0#no person has had a total number of items in front of them that fell within one of the given ranges. 
    return average_wait_time

#The function below gets the total number of items in front of the given person i.
def get_total_items(queue, i):
    #Note that a person j is only in front of the person i if the time person j leaves the queue is after the time person i entered the queue.
    items = queue[4]
    arrival_time = queue[0]
    service_time_end = queue[2]
    drop_out_list = queue[3]

    entered_time = datetime.strptime(arrival_time[i], '%H:%M:%S')#We get the time person i entered the queue
    j = i - 1
    current_total_items = 0#This variable holds the total number of items in front of person i. 
    time_to_compare = datetime.now()

    while j >= 0: 
        #the time person j leaves the queue can either be the service end time of the person j or the drop out time of person j(Depending on whether person j dropped out or not)
        if service_time_end[j] == '0':#we determine if person j dropped out or not. 
            time_to_compare = datetime.strptime(drop_out_list[j], '%H:%M:%S')
        else:
            time_to_compare = datetime.strptime(service_time_end[j], '%H:%M:%S')
        if time_to_compare.time() > entered_time.time():#we determine if person j is in front of person i.
            current_total_items += items[j]
        j -= 1

    return current_total_items

#The get_dropout_probability_ranges function returns an array in which each indexed value contains the probability someone drops out with total items in front of them within the given ranges specified by hlp.itemRange.
def get_dropout_probability_ranges(queue):
    drop_out_list = queue[3]
    items = queue[4]
    arrival = queue[0]
    service_time_end = queue[2]
    drop_out_results = []#The drop out results array will contain an array of dictionaries. Each dictionary has two keys; DroppedOut and DidntDropOut. 
    drop_out_probabilties = []
    for i in range(len(hlp.itemRange)):
        result = {'DroppedOut': 0, 'DidntDropOut': 0}
        drop_out_results.append(result)

    for i in range(len(drop_out_list)):
        dropped_out = False
        current_total_items = get_total_items(queue, i)
        if service_time_end[i] == '0':
            dropped_out = True
        for j in range(len(hlp.itemRange)):
            if current_total_items >= hlp.itemRange[j][0] and current_total_items <= hlp.itemRange[j][1]:
                if dropped_out == True:
                    drop_out_results[j]['DroppedOut'] += 1
                else: drop_out_results[j]['DidntDropOut'] += 1
    
    for i in range(len(drop_out_results)):
        total = float((drop_out_results[i]['DroppedOut'] + drop_out_results[i]['DidntDropOut']))
        if total == 0:
            drop_out_probabilties.append(0)
        else: drop_out_probabilties.append(float(drop_out_results[i]['DroppedOut']) / total)

    return drop_out_probabilties


#The get_dropout_probability function accepts the total number of items in front of a given customer and returns the probability that this person drops out of the line. 
def get_dropout_probability(queue, num_items):
    drop_out_probability_ranges = get_dropout_probability_ranges(queue)
    for i in range(len(drop_out_probability_ranges)):
        if num_items >= hlp.itemRange[i][0] and num_items <= hlp.itemRange[i][1]:
            return drop_out_probability_ranges[i]


#The function defined below accepts the total number of items in front of a given person and returns true if that person drops out and false otherwise.
def bernoulli_drop_out(queue, num_items):
    drop_probability = get_dropout_probability(queue, num_items)
    sample = np.random.uniform(0, 1)
    if sample <= drop_probability:
        return True
    return False

def main():
	Queues=hlp.getData()
	for queue in Queues:
		print(queue)
		print("Droput")
		print(dropout(Queues[queue]))
		print(bernoulli_drop_out(Queues[queue], 50))
		print("")
 
if __name__=="__main__":
	main()