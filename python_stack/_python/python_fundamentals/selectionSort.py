my_array = [64, 34, 25, 5, 22, 11, 90, 12]


def selectionSort(arr):
    length = len(arr)
    for i in range(length - 1):
        min_idx = i
        for j in range(i + 1, length):
            if my_array[j] < my_array[min_idx]:
                min_idx = j
        my_array[i], my_array[min_idx] = my_array[min_idx], my_array[i]


def print_array(arr):
    for val in arr:
        print(val, end=" ")
    print()


print("Original array: ", end="")
print_array(my_array)

selectionSort(my_array)

print("Sorted array: ", end="")
print_array(my_array)