import sys
sys.setrecursionlimit(10000)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n = int(sys.stdin.readline())
graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().strip())))

visited = [[False] * n for _ in range(n)]

def dfs(x, y):
    global count

    graph[x][y] = 0
    count += 1
    import sys
    sys.setrecursionlimit(10000)

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    n = int(sys.stdin.readline())
    graph = []
    for i in range(n):
        graph.append(list(map(int, sys.stdin.readline().strip())))

    visited = [[False] * n for _ in range(n)]

    def dfs(x, y):
        global count

        graph[x][y] = 0
        count += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if graph[nx][ny] == 1:
                dfs(nx, ny)

    result = []
    count = 0

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                count = 0
                dfs(i, j)
                result.append(count)

    result.sort()
    print(len(result))
    for i in result:
        print(i)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue

        if graph[nx][ny] == 1:
            dfs(nx, ny)

result = []
count = 0

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            count = 0
            dfs(i, j)
            result.append(count)

result.sort()
print(len(result))
for i in result:
    print(i)
