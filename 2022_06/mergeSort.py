array = [8,4,6,2,9,1,3,7,5]

## 분할정복, 재귀 이용 알고리즘 --> O(n log n)
## 반으로 쪼개고 다시 합치는 과정에서 그룹을 만들어 정렬, 과정에서 2n개의 공간 필요

def mergeSort(array):
    if len(array) < 2:
        return array
    mid = len(array) // 2
    lowArr = mergeSort(array[:mid])
    highArr = mergeSort(array[mid:])

    mergedArr = []
    l = h = 0
    while l < len(lowArr) and h < len(highArr):
        if lowArr[l] < highArr[h]:
            mergedArr.append(lowArr[l])
            l += 1
        else:
            mergedArr.append(highArr[h])
            h += 1
        print(mergedArr)
    mergedArr += lowArr[l:]
    mergedArr += highArr[h:]
    return mergedArr

array = mergeSort(array)
print(array)