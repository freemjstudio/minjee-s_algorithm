# LCS

a = input()
b = input()
n = len(a)
m = len(b)

array = [[0]*(m+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        if a[i-1] == b[j-1]:
            array[i][j] = array[i-1][j-1] + 1
        else:
            array[i][j] = max(array[i-1][j], array[i][j-1])

print(array[-1][-1]) # 맨 아래 , 맨 오른쪽 원소가 마지막