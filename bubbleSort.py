def bubbleSort(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr)-i):
            if arr[j] > arr[j]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
