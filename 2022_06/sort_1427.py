import sys

N = sys.stdin.readline().strip()

sortedNumber = sorted(list(N))
result = ""

for i in reversed(sortedNumber):
    result += i

print(result)