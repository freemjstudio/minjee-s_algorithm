
n = int(input())

max_dp = [0]*3
min_dp = [0]*3

max_temp = [0]*3
min_temp = [0]*3
for i in range(n):
    a, b, c = map(int, input().split())
    for j in range(3):
        if j == 0:
            max_temp[j] = a + max(max_dp[j], max_dp[j+1])
            min_temp[j] = a + min(min_dp[j], min_dp[j+1])
        elif j == 1:
            max_temp[j] = b + max(max_dp[j], max_dp[j-1], max_dp[j+1])
            min_temp[j] = b + min(min_dp[j], min_dp[j-1], min_dp[j+1])
        else: # j == 2
            max_temp[j] = c + max(max_dp[j], max_dp[j-1])
            min_temp[j] = c + min(min_dp[j], min_dp[j-1])
    for k in range(3):
        max_dp[k] = max_temp[k]
        min_dp[k] = min_temp[k]


print(max(max_dp), min(min_dp))

