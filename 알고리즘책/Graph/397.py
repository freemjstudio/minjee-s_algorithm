# 어두운 길
n, m = map(int, input().split())
edges = []
for i in range(m):
    x, y, cost = map(int, input().split())
    edges.append((cost, x, y)) # 비용 순으로 정렬하기 위해서 cost부터 써준다.

edges.sort() # 비용 순으로 정렬한다.

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, x)
    return parent[x]

def union_find(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

result = 0
total = 0
parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

for edge in edges:
    cost, a, b = edge
    total += cost
    if find_parent(parent, a) != find_parent(parent, b): # 사이클이 발생하지 않는 경우에만 간선에 포함한다. 그러면 최소비용으로 만들 수 있다.
        union_find(parent, a, b)
        result += cost

print(total - result)
