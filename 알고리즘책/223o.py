# 4 바닥공사

n = int(input())
d = [0] * 100

d[1] = 1
d[2] = 3
for i in range(3, n+1):
    d[i] = d[i-1]+2*d[i-2]

print(d[n])
