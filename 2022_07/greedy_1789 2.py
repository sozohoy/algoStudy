N = int(input())
m = 0
result = 0

for i in range(1, N+1):
    result += i
    m += 1
    if (result > N):
        m -= 1import sys

N = list(sys.stdin.readline().strip())

zero_count = 0
one_count = 0
current_number, first_number = int(N[0]), int(N[0])

if first_number == 0: zero_count = 1
else: one_count = 1

for i in range(len(N)):
    if current_number == 0:
        if int(N[i]) != current_number:
            one_count += 1
            current_number = 1
    else:
        if int(N[i]) != current_number:
            zero_count += 1
            current_number = 0

if zero_count >= one_count:
    print(one_count)
else:
    print(zero_count)





        break;

print(m)

