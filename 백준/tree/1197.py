# 1197 최소 스패닝 트리
v, e = map(int, input().split())
edges = []
parent = [0]*(v+1)
for i in range(1, v+1):
    parent[i] = i

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

for i in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
edges.sort() # sort by cost

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
result = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
print(result)
