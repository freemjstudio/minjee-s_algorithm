#1167 트리의 지름
n = int(input())
graph = [[] for _ in range(n+1)]
for i in range(n):
    data = list(map(int, input().split()))
    length = len(data)
    for i in range(1, length-1, 2):
        graph[data[0]].append((data[i],data[i+1])) # next_node, cost

