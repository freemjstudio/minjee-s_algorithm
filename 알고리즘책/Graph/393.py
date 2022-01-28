n, m = map(int, input().split())
graph = []

def find_parent(parent, x):
    if parent[x] != x: # root 가 아니면
        parent[x] = find_parent(parent, x)
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent,a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parent = [0]*(n+1) # 1 ~ n 번까지의 여행지
for i in range(1, n+1):
    parent[i] = i

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[j] == 1: # 1 : 각 노드가 연결되어 있는 상태이므로 union 함수를 실행해서 각 노드의 parent 를 합쳐준다.
            union_parent(parent, i+1, j+1)

data = list(map(int, input().split()))
result = True
for i in range(n-1):
    if find_parent(parent, data[i]) != find_parent(parent, data[i+1]):
        result = False
        break
if result:
    print('YES')
else:
    print('NO')