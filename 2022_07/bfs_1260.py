import sys
from collections import deque

N, M, start = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]

def dfs(start):
    print(start,end=' ')
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(i)
            visited[i] = True

def bfs(start):
    q = deque([start])
    visited[start] = True
    while q:
        now = q.popleft()
        print(now,end=' ')
        for i in graph[now]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(len(graph)):
    graph[i].sort()
visited = [False] * (N+1)
dfs(start)
visited = [False] * (N+1)
print()
bfs(start)
