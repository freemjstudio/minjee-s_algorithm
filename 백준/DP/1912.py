n = int(input())
a = list(map(int, input().split()))
d = [a[0]]
for i in range(len(a)-1):
    d.append(max(d[i] + a[i+1], a[i+1]))

print(max(d))