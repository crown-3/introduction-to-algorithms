# Have the function SecondGreatLow(arr) take the array of numbers stored in arr and return the second lowest and
# second greatest numbers, respectively, separated by a space.
# For example: if arr contains [7, 7, 12, 98, 106] the output should be 12 98.
# The array will not be empty and will contain at least 2 numbers.
# It can get tricky if there's just two numbers!

# Examples
# Input: [1, 42, 42, 180]
# Output: 42 42
#
# Input: [4, 90]
# Output: 90 4

def SecondGreatLow(arr):
    # for more expandability, I will implement the function that finds nth greatest & nth lowest number in array
    nth_greatest, nth_lowest = 2, 2

    # remove duplicates
    arr = list(set(arr))

    # the function exit when the nth_greatest(or nth_lowest) is bigger than the array size; since it doesn't exist
    if len(arr) < nth_greatest or len(arr) < nth_lowest:
        return

    # sort the array so that we can find the nth maximum or mth minimum easily
    arr.sort()

    # built-in cases
    if len(arr) == 1:
        return f"{arr[0]} {arr[0]}"

    if len(arr) == 2:
        return f"{arr[1]} {arr[0]}"

    # normal case
    nth_greatest_num = arr[-nth_greatest]
    nth_lowest_num = arr[nth_lowest - 1]

    return f"{nth_lowest_num} {nth_greatest_num}"


print(SecondGreatLow([1, 42, 42, 180]))  # Output should be "42 42"
print(SecondGreatLow([4, 90]))  # Output should be "90 4"
print(SecondGreatLow([7, 7, 12, 98, 106]))  # Output should be "12 98"
