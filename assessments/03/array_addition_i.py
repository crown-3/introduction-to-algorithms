# Have the function ArrayAdditionI(arr) take the array of numbers
# stored in arr and return the string true if any combination of numbers in the array (excluding the largest number)
# can be added up to equal the largest number in the array,
# otherwise return the string false.
# For example: if arr contains [4, 6, 23, 10, 1, 3]
# the output should return true because 4 + 6 + 10 + 3 = 23.
# The array will not be empty, will not contain all the same elements, and may contain negative numbers.

# Examples
# Input: [5,7,16,1,2]
# Output: false
# Input: [3,5,-1,8,12]
# Output: true

def ArrayAdditionI(arr):
    largest_number = max(arr)
    arr.remove(largest_number)

    minimum_sum = sum(x for x in arr if x < 0)
    maximum_sum = sum(x for x in arr if x > 0)

    dpt_offset = abs(minimum_sum)
    maximum_index = max(abs(largest_number), abs(maximum_sum), abs(minimum_sum)) * 2 + 1

    array_length = len(arr)
    dpt = [[True if x == dpt_offset else False for x in range(maximum_index)] for _ in range(array_length + 1)]

    for y in range(1, array_length + 1):
        for x in range(maximum_index):
            dpt[y][x] = dpt[y - 1][x]  # 현재 원소를 사용하지 않는 경우

            # 현재 원소를 사용하는 경우
            if 0 <= x - arr[y - 1] < maximum_index:
                dpt[y][x] = dpt[y][x] or dpt[y - 1][x - arr[y - 1]]

    return dpt[array_length][largest_number + dpt_offset]


# print(ArrayAdditionI([5, 7, 16, 1, 2]))  # 출력: false
# print(ArrayAdditionI([3, 5, -1, 8, 12]))  # 출력: true
# print(ArrayAdditionI([1, 2, 3, 4]))  # 출력: true
# print(ArrayAdditionI([0, -1]))  # 출력: true
# print(ArrayAdditionI([-1, -42, 4012, 432, 1]))  # 출력: false
# print(ArrayAdditionI([2, -3, -4, 27, 6, 10, -29, 54]))  # 출력: false

print(ArrayAdditionI([13, -1, -5, -8, -10, 11]))  # false
print(ArrayAdditionI([8, -2, 7, -4, -6, -7, 9]))  # true
print(ArrayAdditionI([20, -6, -9, -12, 17, 22]))  # true
