# a

n, m = map(int, input().split())


a = 100 - n
b = 100 - m
c = 100 - (a+b)
d = a*b
if d > 99 :
    q = (d - d%100)//100
    r = d%100
    r1 = c + q
    r2 = r
else:
    q = d // 100
    r = d %100
    r1 = c
    r2 = d
print(a, b, c, d, q, r)
print(r1, r2)

