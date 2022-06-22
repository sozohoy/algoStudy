import sys

N, M = map(int, sys.stdin.readline().strip().split(" "))

tree = list(map(int, sys.stdin.readline().strip().split(" ")))

startIdx, endIdx = 1, max(tree)

while startIdx <= endIdx:
    midIdx = (startIdx + endIdx) // 2
    result = 0
    for i in tree:
        if i >= midIdx:
            result += i - midIdx

    if result >= M:
        startIdx = midIdx + 1
    else:
        endIdx = midIdx - 1

print(endIdx)
