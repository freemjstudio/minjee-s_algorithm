# 팀 결성
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
g = []
parent = [0] * (n+1) # 부모 테이블 초기화
for i in range(0, n+1):
    parent[i] = i

def find_parent(parent, x):
    # root node가 아니라면 루트 노드를 찾을 때까지 재귀적으로 호출한다.
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

for i in range(m):
    x,a,b = input().split()
    if x == '0': # 팀합치기 연산 a, b 같은 팀으로
        union_parent(parent, a, b)
    elif x == '1': # 팀확인하기 연산
        team_a = find_parent(parent, a)
        team_b = find_parent(parent, b)
        if team_a == team_b:
            print('YES')
        else:
            print('NO')