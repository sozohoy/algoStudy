## 알파벳 배열에 넣고
## 2번이면 +1초 = 3초걸림

import sys
alpha = list(sys.stdin.readline().strip())
alphaNumbers = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

count = 0

for i in range(len(alpha)):
    for j in range(len(alphaNumbers)):
        if alpha[i] in alphaNumbers[j]:
            count += (j + 3)

print(count)
