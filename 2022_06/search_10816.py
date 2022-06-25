from collections import Counter
import sys

N = int(sys.stdin.readline())
getCard = list(map(int, sys.stdin.readline().strip().split(" ")))
M = int(sys.stdin.readline())
checkCard = list(map(int, sys.stdin.readline().strip().split(" ")))

count = Counter(getCard)

for i in range(M):
    if checkCard[i] in count:
        print(count[checkCard[i]], end=" ")
    else:
        print(0, end=" ")

# def binarySearch(element, array):
#     startIdx = 0
#     endIdx = len(array) - 1
#
#     while startIdx <= endIdx:
#         midIdx = (endIdx + startIdx) // 2
#
#         if element == array[midIdx]:
#             result[i] = array.count(element)
#             return 0
#
#         elif element < array[midIdx]:
#             endIdx = midIdx - 1
#
#         else:
#             startIdx = midIdx + 1
#
#     return 0