# 21921 Blog

n, x = map(int, input().split())
data = list(map(int, input().split()))
max_value = 0
count = 1 # 기간
if max(data) == 0:
    print("SAD")
else:
    max_value = sum(data[:x]) # 미리 계산을 저장해둔다.
    value = max_value
    for i in range(x, n):
        value -= data[i-x]
        value += data[i]
        if value > max_value:
            max_value = value
            count = 1
        elif value == max_value:
            count += 1
    print(max_value)
    print(count)