import sys

N = int(sys.stdin.readline())

fiboArray = [0, 1]

if N <= 1:
    if N == 0:
        print(0)
    else:
        print(1)

else:
    for i in range(2, N+1):
        count = 0

        count = fiboArray[i-1] + fiboArray[i-2]
        fiboArray.append(count)

    print(int(fiboArray[-1]))