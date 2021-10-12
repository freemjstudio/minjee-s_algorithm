N = int(input())
array = [0] + list(map(int, input().split())) # 카드 가격
d = [10001 for i in range(1001)]
d[0] = 0

for i in range(1,N+1):
    for j in range(1,i+1):
        d[i] = min(d[i], d[i-j] + array[j])

print(d[N])