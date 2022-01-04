n, m = map(int, input().split())
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

numbers = []
for i in range(n):
    numbers.append(min(array[i]))

print(max(numbers))

# 다른 풀이 1
result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)

# 다르풀이 2
result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    result = max(result, min_value)

print(result)