# N = int(input())
#
# array = []
#
# for i in range(N):
#     array.append(int(input()))
#
# for i in range(len(array)):
#     for j in range(len(array)):
#         if array[i] < array[j]:
#             array[i], array[j] = array[j], array[i]
#
# for i in array:
#     print(i)

#
# import sys
#
# N = int(input())
#
# array = []
#
# for _ in range(N):
#     array.append(int(sys.stdin.readline()))
#
# array.sort()
#
# for i in array:
#     print(i)

def mergeSort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left = mergeSort(array[:mid])
    right = mergeSort(array[mid:])

    mergeArray = []
    l = h = 0

    while l < len(left) and h < len(right):
        if left[i] < right[h]:
            mergeArray.append(left[i])
            i += 1

        else:
            mergeArray.append(right[h])
            j +=1

    if i < len(left):
        mergeArray += left[i:]

    if j < len(right):
        mergeArray += right[h:]

    return mergeArray

