max_n = 0
curr = 0
for i in range(10):
    a, b = map(int, input().split())
    curr -= a
    curr += b
    if curr > max_n:
        max_n = curr

print(max_n)