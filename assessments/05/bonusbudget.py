def Bonusbudget(arr):

    # initially assign every worker $1000 bonus
    n = len(arr)
    bonus = [1000] * n

    # increase bonus if arr is higher than previous worker, traversing from left to right
    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            bonus[i] = bonus[i - 1] + 1000

    # this time, do same thing traversing from right to left, comparing each index with the right ones
    for i in range(n - 2, -1, -1):
        if arr[i] > arr[i + 1]:
            bonus[i] = max(bonus[i], bonus[i + 1] + 1000)

    return sum(bonus)


# test cases
print(Bonusbudget([1, 0, 2]))
print(Bonusbudget([12, 4, 3, 11, 34, 34, 1, 67]))
print(Bonusbudget([1, 2, 3, 4, 5]))
print(Bonusbudget([5, 4, 3, 2, 1]))
print(Bonusbudget([5, 5, 5, 5]))
print(Bonusbudget([1, 3, 2, 4, 3]))
print(Bonusbudget([7]))
print(Bonusbudget([-2, -1, -3, -4]))

