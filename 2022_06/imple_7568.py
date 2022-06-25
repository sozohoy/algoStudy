import sys

N = int(sys.stdin.readline())

weight = []
height = []

for _ in range(N):
    data = list(map(int, sys.stdin.readline().strip().split(" ")))
    weight.append(data[0])
    height.append(data[1])

for i in range(N):
    result = 1
    for j in range(N):
        if weight[i] < weight[j] and height[i] < height[j]:
            result += 1
    print(result)