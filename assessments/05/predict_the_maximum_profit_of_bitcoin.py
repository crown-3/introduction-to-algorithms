def PredictthemaximumprofitofBitcoin(arr):
    n = len(arr)
    max_profit = 0

    for i in range(1, n):
        # IDK if I am misunderstanding this problem, this job can be done in this way
        if arr[i] > arr[i - 1]:
            max_profit += arr[i] - arr[i - 1]

    return max_profit
