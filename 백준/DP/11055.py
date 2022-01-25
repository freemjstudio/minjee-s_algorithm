
n = int(input())
array = list(map(int, input().split()))
dp = [i for i in array]

for i in range(n): # 0 ~ 9
    for j in range(i):
        if array[i] > array[j]:
            dp[i] = max(dp[i], dp[j] + array[i])

print(max(dp))
