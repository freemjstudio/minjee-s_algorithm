n = int(input())
t = []
p = []
dp = []

for i in range(n):
    a, b = map(int, input().split()) # 소요 일수, 얻는 비용
    t.append(a)
    p.append(b)
    dp.append(b) # 비용 최대를 구해야하니까 dp는 비용 중심이다 !
dp.append(0)

for i in range(n-1, -1, -1): # (n-1) ... 0
    if t[i] + i > n: # 상담 불가능한 경우지~~~
        dp[i] = dp[i+1] # day 7은 못하니까 걍 8 값 0을 넣엇음 ㅋㅋ
    else: # 상담 가능한 경우 지금 건수를 할지말지잖아
        dp[i] = max(dp[i+1], p[i] + dp[i + t[i]]) #day 5말고 6 , 
print(dp[0])