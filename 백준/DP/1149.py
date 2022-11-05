# rbg 거리 1
n = int(input())
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

for i in range(1, n): # array 내부에서 누적합 계산
    array[i][0] = min(array[i-1][1], array[i-1][2]) + array[i][0] # i번째에 R 선택하는 경우
    array[i][1] = min(array[i-1][0], array[i-1][2]) + array[i][1]
    array[i][2] = min(array[i-1][0], array[i-1][1]) + array[i][2]

# 누적합 중에서 최솟값
print(min(array[n-1][0], array[n-1][1], array[n-1][2]))
