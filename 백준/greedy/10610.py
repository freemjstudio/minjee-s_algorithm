
n = list(input())
total = 0

for i in n:
    total += int(i)
if '0' not in n or total %3 != 0:
    print(-1)
else:
    n.sort(reverse=True)
    print(''.join(n))