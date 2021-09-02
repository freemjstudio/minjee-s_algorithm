from collections import deque

def bfs(graph, start, visited):
    queue = deque([start]) # 시작정점을 큐에 먼저 넣는다!!
    visited[start] = True # 현재 노드를 방문 처리한다
    # 큐가 빌 때까지 반복 !!
    while queue:
        v = queue.popleft() # 큐에서 하나의 원소를 뽑아서 출력한다.
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입한다.
        for i in graph[v]:
            if not visited[i]: # 방문되지 않은 경우 큐에 넣는당
                queue.append(i)
                visited[i] = True # 방문함으로 바꿔준다
