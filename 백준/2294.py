# 2294 동전 2

n, k = map(int, input().split())
d = [99999999] * (k+1) # Minimum 을 구하는 것이므로 INF로 초기화를 해준다 
d[0] = 0
coin = []

for i in range(n):
    coin.append(int(input()))

for i in coin:
    for j in range(i, k+1): # i 보다 작은 경우는 만들수가 없다
       d[j] = min(d[j-i]+1, d[j])

print(d[k] if d[k] != 99999999 else -1)

