# Sorting an array can be done using an iterative method.
# We have also learned divide and conquer methods of sorting an array
# using merge sort and quick sort. But in this question,
#
# you must sort an array using simple recursion.
# You should not care about the time complexity of this question.
# The goal is to teach you how you can think in terms of recursion to solve a given problem.
#
# You must not use min(), max(), sort() functions of python.
# if needed you can write your own min() or max() function,
# again in recursive manner.
#
# You must not use merge sort or quick sort algorithm.
# In your code, you must not have any loops, it should be completely loop free.

def SortanArrayusingrecursion(arr, start=0):
    # I will implement the function that finds the minimum value(index) in arr
    # in recursive manner

    if len(arr) <= 1 or start == len(arr) - 1:
        return arr

    minimum_index = find_minimum_index(arr, start, len(arr) - 1)

    arr[start], arr[minimum_index] = arr[minimum_index], arr[start]

    SortanArrayusingrecursion(arr, start + 1)

    return arr


# this is the minimum-value-finding function
def find_minimum_index(arr, start, end):
    if start == end:
        return start

    minimum_rest = find_minimum_index(arr, start + 1, end)

    return start if arr[start] < arr[minimum_rest] else minimum_rest


# Test the function
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print("Original array:", arr)
sorted_arr = SortanArrayusingrecursion(arr)
print("Sorted array:", sorted_arr)