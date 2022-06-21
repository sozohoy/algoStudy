import sys

N = int(sys.stdin.readline().strip())
checkArray = [0] * 10001

for _ in range(N):
    num = int(sys.stdin.readline())
    checkArray[num] += 1


for i in range(10001):
    if checkArray[i] != 0:
        for j in range(checkArray[i]):
            print(i)




# def quickSort(array):
#     if len(array) <= 1:
#         return array
#
#     pivot = array[len(array) // 2]
#
#     left, right, equal = [], [], []
#
#     for num in array:
#         if num < pivot:
#             left.append(num)
#         elif num > pivot:
#             right.append(num)
#         else:
#             equal.append(num)
#
#     return quickSort(left) + equal + quickSort(right)
# def mergeSort(array):
#     if len(array) <= 1:
#         return array
#
#     mid = len(array) // 2
#     left = mergeSort(array[:mid])
#     right = mergeSort(array[mid:])
#
#     mergeArray = []
#     l = h = 0
#
#     while l < len(left) and h < len(right):
#         if left[l] < right[h]:
#             mergeArray.append(left[l])
#             l += 1
#         else:
#             mergeArray.append(right[h])
#             h += 1
#
#     if l < len(left):
#         mergeArray += left[l:]
#     if h < len(right):
#         mergeArray += right[h:]
#
#     return mergeArray