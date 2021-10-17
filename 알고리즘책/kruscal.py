def find_parent(parent, x): # 부모 찾기
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v+1)

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블에서 자기 자신을 부모로 초기화
for i in range(1, v+1):
    parent[i] = i

for _ in range(e): # 모든 간선에 대한 정보 입력 받기
    a, b, cost = map(int, input().split())
    # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost, a, b))

edges.sort() # edges를 비용 순으로 오름차순 정렬

# 간선을 하나씩 확인함
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)

# 크루스칼 알고리즘은 간선의 개수가 e 일 때 O(ElogE)의 시간 복잡도를 가진다. -> E 개의 데이터를 정렬 했을 때의 시간 복잡도