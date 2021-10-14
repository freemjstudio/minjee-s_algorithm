import sys
input = sys.stdin.readline()
INF = int(1e9) # 10 억

# 노드 간선 개수 입력 받기
n, m = map(int, input().split())
# 시작 노드 번호를 입력 받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n+1)]
# 방문한 적이 있는지 체크하는 목적의 리스트를 만들기
visited = [False]*(n+1)
# 최단거리 테이블을 모두 무한으로 초기화
distance = [INF]*(n+1)

# 간선 정보 입력 받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a 번 노드에서 b번 노드로 가는 비용이 c이다.
    graph[a].append((b, c))

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0 # 가장 최단거리가 짧은 노드 (인덱스)
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True

    for j in graph[start]:
        distance[j[0]] = j[1] # B 지점 까지 가는 거리는 j[1] 에 담겨 있음 [A, (B,C)) 이고 여기서 C가 거리
    # 시작 노드를 제외한 전체 n-1 개의 노드에 대해 반복
    for i in range(n-1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서 방문처리한다
        now = get_smallest_node()
        visited[now] = True # 방문처리
        # 현재 노드와 연결된 다른 노드를 확인한다
        for j in graph[now]:
            cost = distance[now] + j[1] # 현재 지점까지 오는데 걸린 거리를 축적하면서 더해주는거지
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    # 도달 할 수 없는 경우, 무한이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])