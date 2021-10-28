from itertools import combinations

n, m = map(int, input().split())
chicken = []
home = []

for r in range(n): # row 의 길이 n
    data = list(map(int, input().split()))
    for c in range(n): # column의 길이도 n
        if data[c] == 2:
            chicken.append((r, c))
        elif data[c] == 1:
            home.append((r, c))

candidates = combinations(chicken, m)

def solve(candidate):
    result = 0 # 치킨 거리 최종
    for hx, hy in home:
        temp = 1e9
        for cx, cy in candidate:
            temp = min(temp, abs(hx - cx) + abs(hy - cy)) # 한 집에서 가장 가까운 치킨집과의 거리를 구함
        result += temp
    return result

result = 1e9

for candidate in candidates:
    result = min(result, solve(candidate))
print(result)
