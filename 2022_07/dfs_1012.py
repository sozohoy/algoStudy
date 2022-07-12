import sys
# 재귀 함수 사용 시 무조건 사용해야 함. 재귀의 최대 깊이 조정
sys.setrecursionlimit(10000)

def dfs(x, y):
    # 상하좌우 확인하기 위한 좌표.
    # 동, 서, 남, 북
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < M) and (0 <= ny < N):
            if graph[ny][nx] == 1:
                graph[ny][nx] = -1
                dfs(nx, ny)

T = int(sys.stdin.readline())

for i in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    graph = [[0 for i in range(M)] for j in range(N)]
    count = 0

    for j in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        graph[Y][X] = 1

    for x in range(M):
        for y in range(N):
            if graph[y][x] == 1:
                dfs(x, y)
                count += 1

    print(count)
