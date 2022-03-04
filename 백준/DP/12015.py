# 12015 가장 긴 증가하는 부분 수열 2

n = int(input())
array = list(map(int, input().split()))

dp = [0]

for num in array:
    if dp[-1] < num: # num 이 가장 큰 숫자이면 더한다
        dp.append(num)
    else: # binary search
        left = 0
        right = len(dp)
        while left < right: # while 문 종료 조건
            mid = (left+right)//2
            if dp[mid] < num:
                left = mid + 1
            else:
                right = mid
        dp[right] = num

print(len(dp)-1)


