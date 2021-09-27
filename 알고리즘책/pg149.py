# 03. 음료수 얼려먹기


N, M = map(int, input().split())

result = 0
graph = []
for i in range(N):
    graph.append(list(map(int, input())))

def dfs(x,y):
    if x <= -1 or y <= -1 or x>= N or x>=M:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1 # 노드 방문처리

        # 상하좌우 확인하기
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True
    return False
    
for i in range(N):
    for j in range(M):
        if dfs(i,j) == True:
            result += 1
print(result)
