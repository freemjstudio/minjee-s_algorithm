# 11279
import sys
import heapq

N = int(sys.stdin.readline())

heap = []

for _ in range(N):
    x = int(sys.stdin.readline())
    if x != 0:
        heapq.heappush(heap, (-x))
    else:
        try:
            print(-1*heapq.heappop(heap))
        except:
            print(0)