import sys

N = int(sys.stdin.readline())

wordArray = []

for _ in range(N):
    wordArray.append(sys.stdin.readline().strip())

for word in wordArray:
    for j in range(len(word)-1):
        if word.find(word[j]) > word.find(word[j+1]):
            N -= 1
            break

print(N)