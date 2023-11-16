def PlateBreaking(arr):
    k, n = arr

    # initialize DPT to store the minimum number of moves for given k and n
    dp = [[0 for _ in range(n+1)] for _ in range(k+1)]

    # fill the matrix with the maximum number of moves required
    for i in range(1, k+1):
        for j in range(1, n+1):
            dp[i][j] = j

    # update the matrix with the optimized number of moves
    for i in range(2, k+1):
        for j in range(1, n+1):
            for x in range(1, j):
                # checkingg the maximum of two scenarios : breaking or not breaking the plate
                dp[i][j] = min(dp[i][j], 1 + max(dp[i-1][x-1], dp[i][j-x]))

    return dp[k][n]

# Test the function with the provided examples
example1 = [2, 6]
example2 = [3, 14]
result1 = PlateBreaking(example1)
result2 = PlateBreaking(example2)

print(result1)
print(result2)