def biggie_size(numbers):
    for i in range(len(numbers)):
        if numbers[i] > 0:
            numbers[i] = "big"
    return numbers
print(biggie_size([-1, 3, 5, -5]))

def count_positives(numbers):
    count = 0
    for i in range(len(numbers)):
        if numbers[i] > 0:
            count += 1
    numbers[len(numbers)-1] = count
    return numbers
print(count_positives([-1,1,1,1]))
print(count_positives([1,6,-4,-2,-7,-2]))


def sum_total(numbers):
    total = 0
    for number in numbers:
        total += number
    return total
print(sum_total([1,2,3,4]))
print(sum_total([6,3,-2]))


def average(numbers):
    total = 0
    average = 0
    for number in numbers:
        total += number
    average = total / len(numbers)
    return  average
print(average([1, 2, 3, 4, ]))

def length(numbers):
    return len(numbers)
print(length([]))

def minimum(numbers):
    if len(numbers) == 0:
        return False
    min = numbers[0]

    for i in range(1, len(numbers)):
        if numbers[i] < min:
            min = numbers[i]
    return min
print(minimum([37,2,1,-9]))
print(minimum([]))

def maximum(numbers):
    if len(numbers) == 0:
        return False
    max = numbers[0]

    for i in range(1, len(numbers)):
        if numbers[i] > max:
            max = numbers[i]
    return max
print(maximum([37,2,1,-9]))
print(maximum([]))

def ultimate_analysis(numbers):
     math_dict = {"sumTotal": sum_total(numbers), "average": average(numbers), "minimum": minimum(numbers), "maximum": maximum(numbers),"length": length(numbers)}
     return math_dict

print(ultimate_analysis([37,2,1,-9]))

def reverse_list(numbers):
    left = 0
    right = len(numbers) - 1

    while left < right:

        temp = numbers[left]
        numbers[left] = numbers[right]
        numbers[right] = temp

        left += 1
        right -= 1
    return numbers
print(reverse_list([37,2,1,-9]))
