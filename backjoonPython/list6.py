N = int(input())
quiz_OX = []
score = 0
count = 1
for i in range(N):
    quiz_OX = input()
    for B in quiz_OX:
        if B == 'O':
            score = score + count
            count += 1
    print(score)