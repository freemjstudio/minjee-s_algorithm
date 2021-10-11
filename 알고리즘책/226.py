# 5 효율적인 화폐 구성

n, m = map(int, input().split())
d = [10001] * m
array = list(map(int, input().split())) # 화폐 구성

for i in range(len(array)):
    for j in range(array[i], m+1):
        if d[j-array[i]] != 10001: # i-k 원을 만드는 방법이 존재하는 경
            d[j] = min(d[j], d[j-array[i]]+1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])
