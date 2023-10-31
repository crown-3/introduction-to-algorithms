# This dp_helper function checks if there is any subset of arr that the sum of subset is 'target',
# and the length of the subset is 'count'.
# It uses memoization 'memo' to avoid duplicate calculation, and makes the algorithm O(n*m)
def dp_helper(arr, idx: int, target: int, count: int, memo: dict) -> bool:
    if target == 0 and count == 0:
        return True

    if idx < 0 or target < 0 or count < 0:
        return False

    if (idx, target, count) in memo:
        return memo[(idx, target, count)]

    include = dp_helper(arr, idx - 1, target - arr[idx], count - 1, memo)
    exclude = dp_helper(arr, idx - 1, target, count, memo)

    memo[(idx, target, count)] = include or exclude

    return memo[(idx, target, count)]


# This reconstruct_sets function uses a memo dictionary to determine which elements belong to each subset.
def reconstruct_sets(arr, target: int, count: int, memo: dict):
    set1, set2 = [], []

    n = len(arr)
    w = target
    c = count

    for i in range(n - 1, -1, -1):
        if not dp_helper(arr, i - 1, w, c, memo):
            set1.append(arr[i])
            w -= arr[i]
            c -= 1
        else:
            set2.append(arr[i])

    return set1, set2


def ParallelSums(arr):
    n = len(arr)
    total_sum = sum(arr)

    # return -1 if the sum is not even 'cause not possible
    if total_sum % 2 != 0:
        return -1

    # the target sum would be the half of the total sum
    target_sum = total_sum // 2
    count = n // 2

    memo = {}

    if not dp_helper(arr, n - 1, target_sum, count, memo):
        return -1

    set1, set2 = reconstruct_sets(arr, target_sum, count, memo)

    # sort the subsets
    set1.sort()
    set2.sort()

    if len(set1) == 0 or len(set2) == 0:
        return -1

    if set1[0] < set2[0]:
        return ','.join(map(str, set1 + set2))
    else:
        return ','.join(map(str, set2 + set1))


# keep this function call here
print(ParallelSums(input()))
