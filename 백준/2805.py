# 나무 자르기 2805
import sys
N, M = map(int, sys.stdin.readline().split())
woods = list(map(int, sys.stdin.readline().split()))

low = 0
high = max(woods)

while low <= high:
    mid = (low+high)//2
    temp = 0
    for wood in woods:
        if wood > mid:
            temp += wood - mid

    if temp >= M:
        low = mid + 1
    elif temp < M:
        high = mid - 1
print(high)


