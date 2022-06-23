import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().strip().split(" ")))
B = list(map(int, sys.stdin.readline().strip().split(" ")))

result = 0

for i in range(N):
    count = min(A) * max(B)
    result += count
    A.pop(A.index(min(A)))
    B.pop(B.index(max(B)))

print(result)


# for _ in range(N):
#     A = map(int)