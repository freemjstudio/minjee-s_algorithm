# python style 우선순위 큐
import heapq

heap = []

heapq.heappush(heap, "a")
heapq.heappush(heap, "b")
heapq.heappush(heap, "c")

print(heap)

numbers = [1,3,2,8,5,7,6,8]

max_list = []

for num in numbers:
    heapq.heappush(max_list, (-num, num))

while max_list:
    print(heapq.heappop(max_list)[1])