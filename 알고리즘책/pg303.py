from collections import deque
import copy

v = int(input())

graph = [[] for i in range(v+1)]
indegree = [0] * (v+1)

# 각 강의시간
time = [0] * (v+1)

# 간선 정보 입력받기
for i in range(1, v+1): # 과목 개수만큼임
    data = list(map(int, input().split()))
    time[i] = data[0]
    for x in data[1:-1]:
        graph[x].append(i)
        indegree[i] =+ 1


def topology():
    result = []
    q = deque()

    # 진입 차수가 0 인 노드를 큐에 삽입한다
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌때까지 반복
    while q:
        now = q.popleft()
        result = copy.deepcopy(time) # 알고리즘 수행 결과를 담을 리스느 
        # 해당 원소와 연결된 노드들의 진입차수 -1
        for i in graph[now]:
            indegree[i] -= 1
            result[i] = max(result[i], result[now] + time[i])

            if indegree[i] == 0:
                q.append(i)

    # 결과 출력
    for i in range(1, v+1):
        print(result[i])

topology()