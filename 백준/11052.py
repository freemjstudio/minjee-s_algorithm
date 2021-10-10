N = int(input())
d = [0] * (N+1)
cards = [0] + list(map(int, input().split()))

d[1] = cards[1]
for i in range(2, N+1):
    for j in range(1,i+1):
        if d[i] < d[i-j] + cards[j]:
            d[i] = d[i-j]+ cards[j]
print(d[N])