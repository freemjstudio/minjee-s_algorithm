n, m = map(int, input().split())
data = [[0 for _ in range(m+1)]]
for _ in range(n):
    line = [0] + list(map(int, list(input())))
    data.append(line)

# 최대값
result = 0
# 합을 저장할 리스트
s = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        s[i][j] = s[i-1][j] + s[i][j-1] - s[i-1][j-1] + data[i][j]

def cal_sum(x1, y1, x2, y2):
    return s[x2][y2] - s[x2][y1-1] - s[x1-1][y2] + s[x1-1][y1-1]
# 방법 1
for i in range(1, m-1):
    for j in range(i+1, m):
        r1 = cal_sum(1, 1, n, i)
        r2 = cal_sum(1, i+1, n, j)
        r3 = cal_sum(1, j+1, n, m)
        result = max(result, r1*r2*r3)

# 방법 2
for i in range(1, n-1):
    for j in range(i+1, n):
        r1 = cal_sum(1, 1, i, m)
        r2 = cal_sum(i+1, 1, j, m)
        r3 = cal_sum(j+1, 1, n, m)
        result = max(result, r1*r2*r3)

# 방법 3
for i in range(1, m):
    for j in range(1, n):
        r1 = cal_sum(1, 1, n, i)
        r2 = cal_sum(1, i+1, j, m)
        r3 = cal_sum(j+1, i+1, n, m)
        result = max(result, r1*r2*r3)

# 방법 4
for i in range(1, n):
    for j in range(1, m):
        r1 = cal_sum(1, 1, i, j)
        r2 = cal_sum(i+1, 1, n, j)
        r3 = cal_sum(1, j+1, n, m)
        result = max(result, r1*r2*r3)

# 방법 5
for i in range(1, n):
    for j in range(1, m):
        r1 = cal_sum(1, 1, i, m)
        r2 = cal_sum(i+1, 1, n, j)
        r3 = cal_sum(i+1, j+1, n, m)
        result = max(result, r1*r2*r3)

# 방법 6
for i in range(1, n):
    for j in range(1, m):
        r1 = cal_sum(1, 1, i, j)
        r2 = cal_sum(1, j+1, i, m)
        r3 = cal_sum(i+1, 1, n, m)
        result = max(result, r1*r2*r3)
print(result)