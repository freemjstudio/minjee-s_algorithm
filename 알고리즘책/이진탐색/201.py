# 떡볶이 떡 만들기

n, m = map(int, input().split())
a = list(map(int, input().split()))

start = 0
end = max(a)
result = 0
while start <= end:
    total = 0 # 떡의 양
    mid = (start + end)//2
    # 떡의 양 계산
    for i in a:
        if i > mid:
            total += (i-mid)
    if total < m: # 떡의 양이 부족한 경우 더 많이 잘라야 한다 -> h를 줄여본다
        end = mid -1
    else:
        result = mid # 최대한 덜 잘랐을 때를 기록해둔다.
        start = mid +1

print(result)


