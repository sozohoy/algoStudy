import sys

N = int(sys.stdin.readline())
array = sorted(list(map(int, sys.stdin.readline().strip().split())))
X = int(sys.stdin.readline())

start = 0
end = len(array) - 1
result = 0

while start != end:
    if array[start] + array[end] == X:
        start += 1
        result += 1
    elif array[start] + array[end] > X:
        end -= 1
    else:
        start += 1

print(result)



# import sys
# from itertools import combinations
#
# N = int(sys.stdin.readline())
# array = sorted(list(map(int, sys.stdin.readline().strip().split())))
# X = int(sys.stdin.readline())
#
# combination = list(combinations(array, 2))
# result = 0
# for i in range(len(combination)):
#     if sum(combination[i]) == X:
#         result += 1
#
# print(result)