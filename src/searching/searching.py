# TO-DO: Implement a recursive implementation of binary search


def binary_search(arr, target, start, end):
    # Your code here
    if not arr:
        return -1

    middle = start + end // 2

    if arr[middle] == target:
        return middle
    elif target > arr[middle]:
        return binary_search(arr, target, middle + 1, end)
    else:
        return binary_search(arr, target, start, middle - 1)

    # STRETCH: implement an order-agnostic binary search
    # This version of binary search should correctly find
    # the target regardless of whether the input array is
    # sorted in ascending order or in descending order
    # You can implement this function either recursively
    # or iteratively


def agnostic_binary_search(arr, target, order=None, start=0, end=None):
    # Your code here
    if not arr:
        return -1

    if not order:
        if arr[0] > arr[-1]:
            order = "dsc"
        else:
            order = "asc"

    if not end:
        end = len(arr) - 1

    if end < start:
        return -1

    middle = (start + end) // 2

    if arr[middle] == target:
        return middle
    elif target > arr[middle] and order == "asc" or target < arr[middle] and order == "dsc":
        return agnostic_binary_search(arr, target, order, middle + 1, end)
    else:
        return agnostic_binary_search(arr, target, order, start, middle - 1)
