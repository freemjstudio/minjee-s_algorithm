# 2293

n, k = map(int, input().split())
coin = []
d = [0] * (k+1)
d[0] = 1

for i in range(n):
    coin.append(int(input()))

for i in coin:
    for j in range(1, k+1):
        if j-i >= 0:
            d[j] += d[j-i]

print(d[k])



