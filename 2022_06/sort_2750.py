N = int(input())

M = []

for i in range(N):
    M.append(int(input()))

for i in range(len(M)):
    for j in range(len(M)):
        if M[i] < M[j]:
            M[i], M[j] = M[j], M[i]

for i in M:
    print(i)