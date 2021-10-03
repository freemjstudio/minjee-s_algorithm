
N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split()))) # 인접행렬

# 플로이드 - 워셜 알고리즘
for k in range(N): # 중간 노드가 될 노드 번호를 k로 삼는다.
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1 or (graph[i][k] == 1 and graph[k][j] == 1):
                graph[i][j] = 1


for row in graph:
    for col in row:
        print(col, end= " ")
    print()





