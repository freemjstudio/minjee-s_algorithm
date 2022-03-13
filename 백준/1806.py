# 1806 부분합
INF = int(1e9)
n, s = map(int, input().split())
array = list(map(int, input().split()))
sum_array = [0]*(n+1)
for i in range(1, n+1):
    sum_array[i] = sum_array[i-1] + array[i-1]

# 투포인터
start = 0
end = 1
count = INF

while start < n:
    if sum_array[end] - sum_array[start] >= s: # 연속된 수열의 합이 s 이상인 경우
        if end - start < count: # count 최소값 갱신하기
            count = end - start
        start += 1 # start 지점 이동
    else:
        if end != n:
            end += 1
        else: # end == n end가 가장 마지막 인덱스에 있을 때
            start += 1


if count == INF: # 합 s 불가능
    print(0)
else:
    print(count)