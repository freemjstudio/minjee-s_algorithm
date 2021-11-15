n = int(input())
t = [] # time
p = [] # price
dp = [0] * (n+1)

max_value = 0

for _ in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

# 리스트를 뒤에서 부터 거꾸로 확인한다.
for i in range(n-1, -1, -1):
    time = t[i] + i
    if time <= n: # 상담 기간내인 경우
        dp[i] = max(p[i] + dp[time], max_value)
    else: # 상담 기간을 벗어나는 경우
        dp[i] = max_value

print(max_value)