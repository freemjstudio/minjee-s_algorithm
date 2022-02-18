# 2011 암호코드

n = input()
l = len(n)
dp = [0]*(l+1)

if n[0] == "0":
    print(0)
else:
    dp[0] = 1
    dp[1] = 1
    for i in range(2, l+1):
        if int(n[i-1]) > 0: # 한자리수 일 때
            dp[i] += dp[i-1]
        temp = int(n[i-1]) + 10 * int(n[i-2])
        if 10 <= temp < 27:
            dp[i] += dp[i-2]

    print(dp[l]%1000000)