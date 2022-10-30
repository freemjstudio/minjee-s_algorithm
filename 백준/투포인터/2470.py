# 2470 두 용액

n = int(input())
data = list(map(int, input().split()))

data.sort()
value = int(1e9)*2
left = 0
right = n-1
idx1 = 0
idx2 = 0
while left < right:
    # 절댓값이 작은 용액
    if value > abs(data[left] + data[right]):
        value = abs(data[left] + data[right])
        idx1 = left
        idx2 = right
    if data[left] + data[right] < 0:
        left += 1
    else:
        right -= 1

print(data[idx1], data[idx2])
