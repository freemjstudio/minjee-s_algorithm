# 1715
import heapq

n = int(input())
heap = []
for i in range(n):
    data = int(input())
    heapq.heappush(heap,data)

result = 0

while len(heap) != 1:
    one = heapq.heappop(heap)
    two = heapq.heappop(heap) # 카드 더미 두개씩 더해 나가야 하니까
    temp_sum = one + two
    result += temp_sum
    heapq.heappush(heap, temp_sum)
print(result)