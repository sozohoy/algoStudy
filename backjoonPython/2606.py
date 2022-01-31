n = int(input())
m = int(input())

graph = [[0]*n for _ in range(n+1)] # 컴퓨터들 연결을 알리는 배열

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

x[2]

print(graph)

visited_dfs = []

def dfs(graph, cur_node, visited):
    visited.append(cur_node) # 현재 노드를 방문처리
    graph[cur_node].sort() # 현재 노드와 인접한 노드를 확인
    for link_node in graph[cur_node]:
        if link_node not in visited: # 방문하지 않은 노드라면 재귀호출
            dfs(graph, link_node, visited)
                # graph / 2 / 1, 2
dfs(graph, 1, visited_dfs)


print(len(visited_dfs)-2)


