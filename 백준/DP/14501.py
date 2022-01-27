# 14501 퇴사
n = int(input())
t = []
p = []
dp = [0] * (n+1)
for i in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)


for i in range(n-1, -1, -1):
    if i + t[i] > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(p[i] + dp[i + t[i]], dp[i+1]) # 이번 일자 상담을 선택한다 vs 선택하지 않는다

print(max(dp))
