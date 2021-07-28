n, k = map(int, input().split())
result = 0

while True:
    target = (n//k)*k
    result += (n-target) # result는 뭐지 .????
    n = target

    if n < k:
        break
    # k 로 나누기
    result += 1
    n //= k

result += n - 1
print(result)
