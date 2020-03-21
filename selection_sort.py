#Finds and returns the index of the smallest value in an array
def find_smallest_item(array):
    smallest = array[0]
    smallest_index = 0
    for i in range(1, len(array)):
        if array[i] < smallest:
            smallest = array[i]
            smallest_index = i
    return smallest_index

#Runtime:  O(n²) ~ Quadratic 
#Pops the element out of the array and appends it to the new Array in asending order.
def selection_sort(arr):
    newArray = []
    for i in range(len(arr)):
        smallest = find_smallest_item(arr)
        newArray.append(arr.pop(smallest))
    return newArray


print(selection_sort([5,3,6,2,10]))