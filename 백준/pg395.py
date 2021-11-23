g = int(input())
p = int(input())

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

parent = [0] *(g+1)

for i in range(1, g+1):
    parent[i] = i # 자기 자신으로 초기화 함

count = 0

for _ in range(p):
    n = int(input()) # gate num
    data = find_parent(parent, n)
    if data == 0:
        break
    union_parent(parent, data, data-1)
    count += 1

print(count)