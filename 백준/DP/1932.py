# 정수 삼각형
n = int(input())
array = []

for i in range(n):
    array.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            up_left = 0
        else:
            up_left = array[i-1][j-1]
        if i == j:
            up_right = 0
        else:
            up_right = array[i-1][j]
        array[i][j] = array[i][j] + max(up_left, up_right)
print(max(array[n-1]))
