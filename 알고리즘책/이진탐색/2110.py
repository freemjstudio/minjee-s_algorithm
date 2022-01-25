# 2110 공유기 설치


n,c = map(int, input().split())
array = []
for i in range(n):
    array.append(int(input()))
array.sort()
start = 1 # 최소 간격
end = array[-1] - array[0] # 최대 간격
result = 0

while start <= end:
    mid = (start+end)//2 # 4
    count = 1 # 공유기 개수
    value = array[0]
    for i in range(1, n):
        if array[i] >= value + mid:
            value = array[i]
            count += 1
    if count >= c:
        start = mid+1 # 될 수 있는 더 큰 간격이 있는지 호가인
        result = mid
    else:
        end = mid - 1

print(result)