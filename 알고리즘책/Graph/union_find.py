def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x]) # 루트 노드가 아니라면 루트 노드를 찾을 때까지 호출
    return parent[x]

def union_parent(parent, a, b): # 두 원소가 속한 집합을 합치기
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
parent = [0] * (v+1) # 부모 테이블 초기화
for i in range(1, v+1):
    parent[i] = i

for i in range(n):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

