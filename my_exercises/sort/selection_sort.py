def selection_sort(array):
    for i in range(0, len(array)):
        print(array)
        index_of_minimum = i

        for j in range(i + 1, len(array)):
            if array[j] < array[index_of_minimum]:
                index_of_minimum = j

        array[i], array[index_of_minimum] = array[index_of_minimum], array[i]

    return array


arr1 = [7, -30, 3, 6, 2, 90]
print(selection_sort(arr1))