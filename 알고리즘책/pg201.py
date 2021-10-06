# 떡볶이 떡 만들기

N, M = map(int, input().split())
array = list(map(int, input().split()))
start = 0
end = max(array)

result = 0

while(start <= end):
    total = 0
    mid = (start + end)//2
    for x in array:
        if x > mid :
            total += x - mid

    if total < M: # 떡의 양이 모자라면
        end = mid -1 # 더 짧게 짤라서 왼쪽 부분 탐색
    else:
        result = mid # 최대한 덜 짤랐을 때가 정답이므로 여기서 result에 기록한다.
        start = mid + 1



print(result)