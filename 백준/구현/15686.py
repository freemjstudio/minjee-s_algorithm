# 치킨 배달
from itertools import combinations

n, m = map(int, input().split())

home = []
chicken = []

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1:
            home.append((i, j)) # 집의 좌표
        if data[j] == 2:
            chicken.append((i, j)) # 치킨 집 좌표

cases = combinations(chicken, m) # 치킨집 중에서 m개를 선택하는 모든 경우의 수

def check_sum(case):
    result = 0
    for hx, hy in home:
        temp = 1e9
        for cx, cy in case:
            temp = min(temp, abs(hx-cx) + abs(hy-cy))
    result += temp

result = 1e9
for case in cases:
    result = min(result, check_sum(case))

print(result)