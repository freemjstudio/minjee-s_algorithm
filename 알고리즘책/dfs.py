def dfs(graph, v, visited):
    visited[v] = True # 시작 노드
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 각 노드가 방문한 정보를 리스트 자료형 으로 표현한다.
visited = [False]*9


