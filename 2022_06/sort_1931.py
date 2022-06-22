import sys

N = int(sys.stdin.readline())

array = []

for _ in range(N):
    split = sys.stdin.readline().strip().split(" ")
    array.append([int(split[0]), int(split[1])])

print(list(set(sorted(array))))