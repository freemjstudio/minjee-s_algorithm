# 14719 빗물

h, w = map(int, input().split())
block = list(map(int, input().split()))

# 투포인터로 풀기
left = 0
right = w-1
left_max = block[left]
right_max = block[right]

volume = 0
while left < right:
    left_max = max(left_max, block[left])
    right_max = max(right_max, block[right])

    if left_max <= right_max:
        volume += left_max - block[left]
        left += 1
    else:
        volume += right_max - block[right]
        right -= 1

print(volume)