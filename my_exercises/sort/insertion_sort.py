def insertion_sort(array):
    for i in range(1, len(array)):
        target = array[i]

        j = i - 1
        while 0 <= j and target <= array[j]:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = target
    return array


arr1 = [5, 2, 4, 7, 1, 3, 2, 6]
print(insertion_sort(arr1))