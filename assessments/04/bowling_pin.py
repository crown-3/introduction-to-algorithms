def BowlingPin(arr):
    n = len(arr)

    # for simplify the calculation, add 1 on each side
    arr = [1] + arr + [1]

    # Initialize a 2D array for dynamic programming
    dp = [[0 for _ in range(n + 2)] for _ in range(n + 2)]

    # setup DPT
    for length in range(1, n + 1):
        for left in range(1, n - length + 2):
            right = left + length - 1
            for i in range(left, right + 1):
                # calculate score for hitting the ith pin
                score = arr[left - 1] * arr[i] * arr[right + 1]
                # update the dp table with the maximum score
                dp[left][right] = max(dp[left][right], dp[left][i - 1] + score + dp[i + 1][right])

    # the answer is in the top right corner of the dp table
    return dp[1][n]


print(BowlingPin([3, 1, 5, 8]))
print(BowlingPin([1, 5]))
print(BowlingPin([]))
print(BowlingPin([0, 0, 0]))

