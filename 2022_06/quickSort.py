## 재귀 알고리즘
## 복잡도 O(n log n)
## pivot 사용

array = [6, 5, 1, 4, 7, 2, 3]


def quickSort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    leftArr, equalArr, rightArr = [], [], []
    for num in arr:
        if num < pivot:
            leftArr.append(num)
        elif num > pivot:
            rightArr.append(num)
        else:
            equalArr.append(num)

    return quickSort(leftArr) + equalArr + quickSort(rightArr)

array = quickSort(array)
print(array)