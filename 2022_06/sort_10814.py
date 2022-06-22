import sys

N = int(sys.stdin.readline())

array = []

for _ in range(N):
    xySplit = sys.stdin.readline().strip().split(" ")
    array.append([int(xySplit[0]), xySplit[1]])

array.sort(key=lambda x: x[0])
for i in array:
    print(i[0], i[1])

