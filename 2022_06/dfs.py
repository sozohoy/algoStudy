graph = dict()

graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

def dfs(graph, startNode):

    ## 항상 두개의 리스트를 별도로 관리, 방문한 리스트 방문 해야 하는 리스트.
    needVisited, visited = list(), list()
    ## 시작 노드 설정
    needVisited.append(startNode)
    ## 방문이 필요한 노드가 있을 경우
    count = 0
    while needVisited:
        count += 1
        print(count)
        print("while문 내부")

        ## 그 중 가장 마지막 데이터를 추출(스택 구조 활용)
        node = needVisited.pop()
        print(needVisited, node, visited)

        ## 위의 노드를 방문한 적 없 을 경우
        if node not in visited:
            visited.append(node)
            ## 그 노드에 연결된 노드들을 needVisited에 extend
            needVisited.extend(graph[node]) # 괄호가 빠진 상황 ex ["p", "q"]를 A에 extend시 ['B', 'C', 'p', 'q']
            print("if문 내부")
            print(visited, needVisited)
    return visited


print(dfs(graph, 'A'))