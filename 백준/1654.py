# 1654
import sys

K, N = map(int, sys.stdin.readline().split())
lan_list = [int(sys.stdin.readline()) for _ in range(K)]

high = max(lan_list)
low = 1
while low <= high:
    count = 0
    mid = (high+low)//2
    for lan in lan_list:
        count += lan//mid

    if count >= N:
        low = mid + 1
    else:
        high = mid -1
print(high)