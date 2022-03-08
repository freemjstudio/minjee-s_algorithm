# 2839 설탕 배달

n = int(input())
dp = [0]*(n+1)
result = 0

while n >= 0:
    if n % 5 == 0:
        result += (n//5)
        print(result)
        break
    n -= 3
    result += 1
else:
    print(-1)

a, b = map(int, input().split())
print(a+b)


