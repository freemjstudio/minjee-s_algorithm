n, m = map(int, input().split())
data = list(map(int, input().split()))

result = 0
for i in range(len(data)):
    for j in range(i+1, len(data)):
        if data[i] != data[j]:
            result += 1

print(result)

# 다른 풀이

# 1 부터 10까지의 무게를 담을 수 있는 리스트
array = [0] * 11

for x in data:
    array[x] += 1 # 각 무게에 해당하는 볼링공의 개수를 카운트 한다

result = 0
# 1부터 m 까지 각 무게에 대해서 처리
for i in range(1, m+1):
    n -= array[i]
    result += array[i] * n
    