##Week 4 Task 1

##Adapt the binary search algorithm so that instead of outputting whether
##a specific value was found, it outputs whether a value within an interval was found

##PSEUDOCODE

#Generate list of random numbers (list)
#Prompt user for range to search for (rangemax, rangemin)
#Put pointers on top and bottom of list (high, low)

#FUNCTION binary_search
#	IF high - low < 0 then
#		PRINT "False"
#	Else
#		Take center point of the list(MIDDLE)
#		IF MIDDLE >= Rangemin and MIDDLE <= highvalue
#			PRINT "True"
# 		Elif Rangemax <= MIDDLE 
#			RETURN FUNCTION(list, rangemax, rangemin, low, MIDDLE-1)
#		Elif Rangemin >= MIDDLE
#			RETURN FUNCTION(list, rangemax, rangemin, high, MIDDLE+1)

import random
#lst = [1, 2, 4, 5, 7, 11, 13, 15, 17, 22, 24, 34, 39, 44, 50]
lst = [0, 1, 2, 8, 13, 17, 19, 32, 42]
#lst = random.sample(range(0, 50), 20)
#lst.sort()
lowvalue = int(input("Input lower bound")) 
highvalue = int(input("Input higher bound"))
high = len(lst) - 1 #Pointer to end of list
low = 0 #Pointer to bottom of list
def binary_search(lst, lowvalue, highvalue, low, high):
        if high - low < 0:
                print("False")
        else:
                middle = int((low + high) / 2 + 0.5)
                #print(middle)
                if lst[middle] >= lowvalue and lst[middle] <= highvalue:
                        print("True")
                elif highvalue <= lst[middle]:
                        return binary_search(lst, lowvalue, highvalue, low, middle-1)
                elif lowvalue >= lst[middle]:
                        return binary_search(lst, lowvalue, highvalue, middle+1, high)

print(lst)
binary_search(lst, lowvalue, highvalue, low, high)

##Big O Runtime = O(Log(n))
