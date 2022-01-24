# 9465 스티커

t = int(input())
for _ in range(t):
    n = int(input())
    array = []
    for i in range(2):
        array.append(list(map(int, input().split())))
    for i in range(1, n):
        if i == 1:
            array[0][i] += array[1][i-1]
            array[1][i] += array[0][i-1]
        else:
            array[0][i] += max(array[1][i-1], array[1][i-2])
            array[1][i] += max(array[0][i-1], array[0][i-2])


    print(max(array[0][n-1], array[1][n-1]))






