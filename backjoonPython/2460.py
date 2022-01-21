N = []
M = []
for _ in range(10):
    n, m = map(int, input().split())
    N.append(n)
    M.append(m)
max = M[0]
cnt = 0
for i in range(1, (len(N)-1)):
    cnt = int(N[i+1]) + int(M[i])
    if max < cnt:
        max = cnt
print(max)