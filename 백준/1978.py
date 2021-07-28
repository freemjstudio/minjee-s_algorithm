n = int(input())
data = list(map(int, input().split()))

result = 0
for i in data:
    num = 2
    while True:
        if num > i:
            break
        if i % num == 0:
            if num == i :
                result += 1
                break
            else:
                break
        num += 1

print(result)


