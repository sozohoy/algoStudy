import sys

N = int(sys.stdin.readline())
array = []
result = []

for i in range(N):
    array.append(sys.stdin.readline().strip())

for i in range(N):
    count = 0
    print(array[i])

    for j in array[i]:

        if j == "(":
            count += 1

        elif j == ")":
            count -= 1

        if count < 0:
            result.append(0)
            break
    if count > 0:
        result.append(0)

    elif count == 0:
        result.append(1)

print(result)

for i in range(len(result)):
    if result[i] == 1:
        print("YES")
    else:
        print("NO")