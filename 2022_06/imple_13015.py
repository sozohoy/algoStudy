import sys

N = int(sys.stdin.readline())

for i in range(1,(N*2)):
    mid = (N*2) // 2
    if i == 1 or i == (N*2)-1:
        print("*" * N + " " * ((2*N) - 3) + "*" * N)

    else:
        if i < mid:
            print(" " * (i-1) + "*" + " " * (N-2) + "*" + " " * (2 * (N - i) - 1) + "*" + " " * (N-2) + "*")
        elif i > mid:
            print(" " * ((N*2 -1) - i) + "*" + " " * (N-2) + "*" + " " * (2*i - N*2 - 1) + "*" + " "*(N-2) + "*")
        else:
            print(" " * (N-1) + "*" + " " * (N-2) + "*" + " " * (N-2) + "*")
