# 2581 소수

n = int(input())
m = int(input())
result = []
total = 0

def check(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

for num in range(n, m+1):
    if num == 1:
        continue

    if check(num):
        result.append(num)
        total += num

if len(result) == 0:
    print(-1)
else:
    print(sum(result))
    print(min(result))