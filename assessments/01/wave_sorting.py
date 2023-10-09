# Have the function WaveSorting(arr) take the array of positive integers stored in arr and return the string true if
# the numbers can be arranged in a wave pattern: a1 > a2 < a3 > a4 < a5 > ..., otherwise return the string false.
# For example, if arr is: [0, 1, 2, 4, 1, 4],
# then a possible wave ordering of the numbers is: [2, 0, 4, 1, 4, 1].
# So for this input your program should return the string true.
# The input array will always contain at least 2 elements.
# More examples are given below as sample test cases.

# Examples
# Input: [0, 1, 2, 4, 1, 1, 1]
# Output: false
#
# Input: [0, 4, 22, 4, 14, 4, 2]
# Output: true

def WaveSorting(arr):
    # we can make a wave pattern with any array that meets the condition
    # by doing this
    #
    # arr.sort()
    # for i in range(1, len(arr), 2):
    #     arr[i], arr[i - 1] = arr[i - 1], arr[i]
    #
    # (swapping adjacent elements)

    # But the wave pattern is not possible,
    # if any number occurs more than half the length of the array

    # to examine, I will implement a dictionary counting all the numbers
    num_count = {}
    for item in arr:
        if item not in num_count:
            num_count[item] = 1
        else:
            num_count[item] += 1

    for each_count in num_count.values():
        if each_count > len(arr) // 2:
            return "false"

    return "true"


# Examples
print(WaveSorting([0, 1, 2, 4, 1, 1, 1]))  # Output should be "false"
print(WaveSorting([0, 4, 22, 4, 14, 4, 2]))  # Output should be "true"
print(WaveSorting([0, 1, 2, 4, 1, 4]))  # Output should be "true"

