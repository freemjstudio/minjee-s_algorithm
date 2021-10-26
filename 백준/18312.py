n, k = map(int, input().split())

h = ''
m = ''
s = ''

count = 0
for i in range(n+1):
    if i < 10:
        h = '0'+str(i)
    else:
        h = str(i)
    for j in range(60):
        if j < 10:
            m = '0'+ str(j)
        else:
            m = str(j)
        for z in range(60):
            if z < 10:
                s = '0'+str(z)
            else:
                s = str(z)
            if str(k) in h or str(k) in m or str(k) in s:
                count += 1
print(count)