# 397

total_cost = 0
sum_cost = 0 # 우리가 사용해야 하는 비용

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [0] * (n+1)
edges = []

for i in range(1, n+1):
    parent[i] = i

for _ in range(m):
    x, y, cost = map(int, input().split())
    edges.append((cost, x, y))
    total_cost += cost

edges.sort()

# 크루스칼로 최소 비용을 찾는다
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        sum_cost += cost

print(total_cost-sum_cost)