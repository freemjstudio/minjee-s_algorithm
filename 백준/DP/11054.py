# 11054 가장 긴 바이토닉 수열

n = int(input())
array = list(map(int, input().split()))
dp = [1]*n
dp2 = [1]*n
dp3 = [0]*n
# 증가하는 수열
for i in range(n):
    for j in range(i):
        if array[i] > array[j]:
            dp[i] = max(dp[i], dp[j] +1)

max_index = 0
max_length = 0

for i in range(n):
    if dp[i] > max_length:
        max_length = dp[i]
        max_index = i

# 감소하는 수열
for i in range(n-1, -1, -1):
    for j in range(i+1, n):
        if array[i] > array[j]:
            dp2[i] = max(dp2[i], dp2[j]+1)

for i in range(n):
    dp3[i] = dp[i] + dp2[i] -1
print(max(dp3))