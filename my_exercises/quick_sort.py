def quick_sort(array, l, h):
    if l < h:
        j = partition(array, l, h)
        # 주의 : j - 1로 안 하면 이미 된 정렬도 계속 포함시키기 때문에 재귀 호출이 무한히 반복된다.
        # 수만 교수님 의사코드에는 결함이 많은 것 같다...
        quick_sort(array, l, j - 1)
        quick_sort(array, j + 1, h)


def partition(array, l, h):
    print(array, end=" -> ")

    pivot = array[l]

    # "i, j"는 각각 array의 양쪽 끝을 가리킨다. 이제 서서히 가까워지며 값을 비교하고 바꿀 것이다.
    # 맨 왼쪽 값이 pivot이기 때문에 i는 l + 1을 할당한다.
    i, j = l + 1, h

    while True:
        while i <= j and array[i] <= pivot:
            i += 1
        while i <= j and array[j] > pivot:
            j -= 1
        if i > j:
            break
        array[i], array[j] = array[j], array[i]

    array[l], array[j] = array[j], array[l]

    print(array)

    return j


array1 = [6, 8, 2, 7, 7, 1]
quick_sort(array1, 0, len(array1) - 1)
print(array1)
