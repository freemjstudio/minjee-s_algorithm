# 149pg
n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))



def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0: # 아직 노드를 방문하지 않았다면
        graph[x][y] = 1
        # 상하좌우도 조사한다
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return True # 어쨌든 노드는 아이스크림을 만들 수 있으므로 true 반환하는데...
    return False # 1이면 false

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            print(graph)
            result += 1
print(result)

