import sys

N = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
array.sort()

M = int(sys.stdin.readline())
elementArray = list(map(int, sys.stdin.readline().split()))

for element in elementArray:
    startIndex = 0
    endIndex = len(array) - 1

    while startIndex <= endIndex:
        midIndex = (startIndex + endIndex) // 2

        if element == array[midIndex]:
            print(1)
            break
        elif element < array[midIndex]:
            endIndex = midIndex - 1
        else:
            startIndex = midIndex + 1
        if startIndex > endIndex:
            print(0)
            break



#
# def binarySearch(element, array):
#     startIndex = 0
#     endIndex = len(array) - 1
#
#     while startIndex <= endIndex:
#         midIndex = (startIndex + endIndex) // 2
#
#         if element == array[midIndex]:
#             return 1
#         elif element < array[midIndex]:
#             endIndex -= 1
#         else:
#             startIndex += 1
#     return 0