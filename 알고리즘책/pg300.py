v, e = map(int, input().split())
parent = [[0] * (v+1)]

for i in range(v+1):
    parent[i] = i

def find_parent(parent, x):
    if parent[x] != x:
        find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 간선의 정보
edges = []
# 최종 변수
result = 0
for i in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b)) # 오름 차순 정렬을 하기 위해서 이렇게 cost를 첫번쨰 원소로 설정한다

edges.sort() # cost 순으로 간선을 정렬한다
max_cost = 0 # 비용이 가장 큰 간선

# 간선을 하나씩 확인하며 사이클이 발생하지 않는 경우만 집합에 포함시킨다

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        max_cost = cost
        
print(result - max_cost)


