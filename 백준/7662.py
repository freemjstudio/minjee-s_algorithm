# 7662 우선순위 큐 그런데 이중을 곁들인
import heapq
import sys
N = int(input())
for _ in range(N):
    max_heap = []
    min_heap = []
    visit = [False]*1_000_001
    T = int(sys.stdin.readline())
    for key in range(T):
        query = list(input().split())
        if query[0] == 'I':
            heapq.heappush(min_heap, (int(query[1]), key))
            heapq.heappush(max_heap, (int(query[1])*(-1), key))
            visit[key] = True

        elif query[0] == 'D':
            if query[1] == '-1':
                while min_heap and not visit[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    visit[min_heap[0][1]] = False
                    heapq.heappop(min_heap)
            elif query[1] == '1': # 최대힙에서 pop
                while max_heap and not visit[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    visit[max_heap[0][1]] = False
                    heapq.heappop(max_heap)

    while min_heap and not visit[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visit[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if min_heap and max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print("EMPTY")