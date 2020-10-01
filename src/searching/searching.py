def linear_search(arr, target):
    # Your code here
    if len(arr) == 0:
        return -1
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i
    return -1


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    arr.sort()

    begin = 0
    end = len(arr) - 1

    while begin <= end:
        middle = int((begin + end) / 2)
        if target < arr[middle]:
            end = middle - 1
        elif target > arr[middle]:
            begin = middle + 1
        else:
            return middle
    return -1  # not found

test = [2, 3, 6, 8, 99, 7]

# print(linear_search(test, 100))

print(binary_search(test, 8))