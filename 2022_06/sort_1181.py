import sys
## strip은 이시기 뭐시기를 해줌
n = int(input())

array = []

for _ in range(n):
    array.append(sys.stdin.readline().strip())

setArray = list(set(array))
sortedArray = []

for i in setArray:
    sortedArray.append((len(i), i))

sortedString = sorted(sortedArray)

result = []
for num, word in sortedString:
    result.append(word)

for i in result:
    print(i)