d = [0] * 100
def pido(x):
    if (x == 1 or x == 2):
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = pido(x-1) + pido(x-2)
    return d[x]


# 재귀적 방법은 위
d[1] = 1
d[2] = 1

n = 99
for i in range(3,n+1):
    d[i] = d[i-1] + d[i-2]

print(d[6])