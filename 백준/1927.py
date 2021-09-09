# 1927
from collections import deque
N = int(input())
queue = deque()
for _ in range(N):
    i = 1 # index

    num = int(input())
    if num == 0:  # 0 입력 되면 min 값을 출력하고 배열에서 제거한다
        if not queue: # queue 비어있는지 확인하기
            print(0)
        else:
            temp = queue.popleft()
            print(temp)
    else:
        # 우선순위 큐에 삽입하기
        while i<=N:
            if num >= queue[i]:

        queue[i] = num


import sys
import heapq

N = int(sys.stdin.readline())
heap = []
for _ in range(N):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(heap, num)
    else:
        try:
            print(heapq.heappop(heap))
        except: # heap 이 empty인 경우 예외처리를 try-except문으로 커버 가능하다 와웅
            print(0)