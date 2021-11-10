N , M = map(int, input().split())
t = list(map(int, input().split()))
count = 0
sumAB = 0
for i in range(N-2):
    for j in range(1, N-1):
        for k in range(2, N):
            if t[i] != t[j] and t[i] != t[k] and t[j] != t[k]:
                sumAB = t[i] + t[j] + t[k]
            if sumAB > count and sumAB <= M:
                count = sumAB
print(count)
