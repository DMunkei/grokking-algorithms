import random 
#Quicksort is a recursive algorithm that follows the Divide and Conquer principle.
#Runtime: Worst case O(n²) - Average case O(n*log n)
#1. Figure out your base case
#2. Divide or decrease your problem until it becomes the base case!

def bubblesort(arr):
    for x in range(len(arr)):
        for i in range(0, len(arr)-x-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr


#You start of by picking a "Pivot", this is a random element in the array to perform the comparism with,
#Elements smaller than the Pivot get put on the left, elements greater onto the right
def quicksort(arr):       
    if len(arr) < 2:
        return arr #Base case - The elements with 0 or 1 elements are already taken as sorted
    else:# The recursive case 
        # Taking the first element as a pivot might not be beneficial, probably taking an element in the middle is more efficient?
        # Since the algorithm gets slower the larger your 'Call stack' becomes. Call Stack depth = Worst case: O(n) - Average Case: O(n*log n)
        #rand =random.randint(0,(len(arr)-1)) 
        #pivot = arr[rand]
        pivot = arr[0] 
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater) #It first calls the qsort on less then greater until it reaches the base case and its done

import time 
print("Quicksort")
start = time.time()
print(quicksort([5,6,1,69]))
end = time.time()
print(end-start)
# print("-"*80)
# print("Bubblesort")
# start = time.time()
# print(bubblesort([5,6,10,2,3,4,5,6,2,2,0,3,200,4,44123,44000,9458585,987564,3213210,150,0,48977,15197,112,665,445,666,7787,4521,15975651,32465789,12313465,7,2923450,81289319823,8858581,2,345,69878,1,203,9,85892,76823845,12,]))
# end = time.time()
# print(end-start)


#Excercise 4.1
def sum(arr):
    total = 0
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return arr[0] 
    total = arr.pop(0) + sum(arr)
    return total

#Ex 4.2 count items in list 
def count(arr):
    total = 0
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return 1
    #total = 1 + (0*arr.pop(0)) + count(arr) This is more of a mathematical "approach", since 0 is the Multiplicative Annihilator 0 * i = 0 = i * 0
    #total = 1 + count(arr[1:])#More Pythonic way of reducing the size of the array - removes first entry
    total = 1 + count(arr[:-1])#More Pythonic way of reducing the size of the array - removes last entry
    return total

# find the max number in an array
def max(arr):
    max = 0
    for i in arr:
        if max < i:
            max = i
    return max

# def recursive_max(arr):
#     max = 0
#     if len(arr) == 0:
#         return None
#     elif len(arr) == 1:
#         return arr[0]
#     if max < arr[0]:
#         max = 
#     else:
#         max = recursive_max(arr[1:])
#     return max

#print(sum([2,4,6]))
#print(count([2,4,6,4,5,0,0]))
#print(max([2,4,6,4,5,0,0,9]))
#print(recursive_max([2,4,6,4,5,0,0,9]))