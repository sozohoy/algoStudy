import sys

N = int(sys.stdin.readline())
getCard = list(map(int, sys.stdin.readline().strip().split(" ")))
M = int(sys.stdin.readline())
checkCard = list(map(int, sys.stdin.readline().strip().split(" ")))

getCard.sort()
result = []

def binarySearch(element, array):
    startIdx = 0
    endIdx = len(array) - 1

    while startIdx <= endIdx:
        midIdx = (endIdx + startIdx) // 2

        if element == array[midIdx]:
            result.append(1)
            return 0

        elif element < array[midIdx]:
            endIdx = midIdx - 1

        else:
            startIdx = midIdx + 1

    result.append(0)
    return 0

for i in range(M):
    binarySearch(checkCard[i], getCard)
    print(result[i], end=' ')


# for i in range(M):
#     if checkCard[i] in getCard:
#         result.append(1)
#     else:
#         result.append(0)
#
# print(result)