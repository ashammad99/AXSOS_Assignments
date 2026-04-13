#Countdown
def countdown(n):
    myList = []
    while n >= 0:
        myList.append(n)
        n -= 1
    return myList
print(countdown(5))

# Print and Return
def print_and_return(n):
    print(n[0])
    return n[1]
print(print_and_return([1,5]))


def first_pluse_length(myList):
    return len(myList) + myList[0]

print(first_pluse_length([1,2,3,4,5]))

def values_greater_than(myList):
	if len(myList) < 2:
        return False
		
    newList = []
    for i in range(len(myList)):
        if myList[i] > myList[1]:
            newList.append(myList[i])
    print(len(newList))
    return newList
print(values_greater_than([5,2,3,2,1,4]))


def length_and_value(size,value):
    myList = []
    for i in range(size):
        myList.append(value)
    return myList
print(length_and_value(6,2))
print(length_and_value(4,7))

