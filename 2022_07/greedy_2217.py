import sys

N = int(sys.stdin.readline())
array = []

for i in range(N):
    array.append(int(sys.stdin.readline()))

array.sort()
for i in range(N):
    array[i] = array[i] * (N-i)
# 모든 로프를 사용해야할 필요는 없으며, 임의의 몇개의 로프를 사용해도 된다.
print(max(array))