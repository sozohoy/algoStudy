import sys

N = int(sys.stdin.readline())

array = []

for _ in range(N):
    xyNum = sys.stdin.readline().strip().split(" ")
    array.append([int(xyNum[0]), int(xyNum[1])])

result = sorted(array)

for i in range(N):
    print(result[i][0], result[i][1])
