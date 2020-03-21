#Variables inside of functions being called remain in memory
#aslong as the function call is not resolved.
#Downside to recursion, uses a lot of memory!


def countdown(i):
    if i == 0: #This needs to be inside as our base case.To end the recursion! 
        return
    print(i)
    countdown(i-1)

def factorial(x):
    if x == 1:#Base case to end recursion
        return 1
    return x * factorial(x-1)

countdown(5)
