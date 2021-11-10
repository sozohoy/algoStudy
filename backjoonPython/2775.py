T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    peopleList = [[0] * 15 for k in range(15)]

    for x in range(15):
        peopleList[0][x] = x + 1
        peopleList[x][0] = 1
    for i in range(1,15):
        for j in range(1,15):
            peopleList[i][j] = peopleList[i][j-1] + peopleList[i-1][j]

    print(peopleList[k][n-1])


#1410
#136
#123