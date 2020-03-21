#Runtime: O(log n) ~ Logarithmic runtime
#If n=1,000,000,000  then the runtime would be 32ms
#Because  of Log2(n)

def binary_search(arr, target):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == target:
            return mid
        if guess > target:
            high = mid-1
        else:
            low = mid+1
    return None

my_list = [1,3,5,7,9]

print(binary_search(my_list, 3))

print(binary_search(my_list, -1))

