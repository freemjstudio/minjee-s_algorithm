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

