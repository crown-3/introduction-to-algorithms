import math
import time


def merge_sort(array, p, r):
    if p < r:
        q = math.floor((p + r) / 2)
        arr1 = merge_sort(array[0:q + 1], 0, q - p)
        arr2 = merge_sort(array[q + 1:r + 1], 0, r - q - 1)

        merged_arr = merge(arr1, arr2)
        print(f"{arr1} + {arr2} = {merged_arr}")

        return merged_arr
    else:
        return [array[p]]


def merge(arr1, arr2):
    arr = []

    # "i, j"는 각각 arr1, arr2의 인덱스를 가리킨다.
    i, j = 0, 0

    # 먼저 arr1과 arr2의 첫번째 원소를 비교하여 작은 원소를 arr에 추가한다.
    # 마치 두 파일의 카드를 비교하여 작은 카드를 새로운 파일에 추가하는 것과 같다.
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            arr.append(arr1[i])
            i += 1
        else:
            arr.append(arr2[j])
            j += 1

    # Combining Remaining elements
    while i < len(arr1):
        arr.append(arr1[i])
        i += 1

    while j < len(arr2):
        arr.append(arr2[j])
        j += 1

    print(arr)

    return arr


array1 = [6, 8, 2, 7, 7, 1]
print(merge_sort(array1, 0, len(array1) - 1))
