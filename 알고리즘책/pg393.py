


# 툭정 원소가 속한 집합을 찾는다
def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 여행지 개수와 여행 계획에 속한 여행지의 개수 입력받기
n, m = map(int, input().split())
parent = [0] * (n+1) # 부모 테이블 초기화

for i in range(1, n+1):
    parent[i] = i

#union 연산을 수행한다 -> 연결되어 있으면 union
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1:
            union_parent(parent, i+1, j+1)

# 여행 계획 입력 받기
plan = list(map(int, input().split()))

# 결과 확인하기
result = True

for i in range(m-1):
    if find_parent(parent, plan[i]) != find_parent(parent, plan[i+1]):
        result = False

if result:
    print('YES')
else:
    print('NO')