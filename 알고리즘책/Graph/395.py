g = int(input()) # 탑승구 1 ~ G번까지의 번호로 구분
p = int(input()) # 비행기 개수

parent = [0] * (g+1) # 탑승구 node 들

for i in range(1, g+1): # 현재 node 들 각각은 자기 자신을 가리키고 있다.
    parent[i] = i

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, x)
    return parent[x]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

result = 0

for _ in range(p):
    data = find_parent(parent, int(input()))
    if data == 0:
        break
    union(parent, data, data-1) # 바로 왼쪽의 집합과 합쳐준다.
    result += 1

print(result)