# 11047
import sys

N, K = map(int, sys.stdin.readline().split())
money = list()
count = 0

for i in range(N):
    num = int(sys.stdin.readline())
    money.append(num)

for i in range(N-1,-1,-1):
    if K == 0:
        break
    if money[i] > K:
        continue
    count += K//money[i]
    K %= money[i]
print(count)

