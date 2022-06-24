import sys

# 2440
# N = int(sys.stdin.readline())
# for i in range(N, 0, -1):
#     print("*" * i)

# 2441
N = int(sys.stdin.readline())
for i in range(N, 0, -1):
    space = N - i
    print(" " * space + "*" * i)