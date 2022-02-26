n = int(input())
array = [[1,1],[1,0]] # 초기 행렬
# 피보나치 수열 초기 값
pibo = [[1], [1]]

def power(array, n):
    if n == 1:
        return array
    elif n%2 == 0:
        return multi(power(array, n-1), array)
    else:
        return power(multi(array, array), n//2)

def multi(a, b): # 행렬의 곱셈
    temp = [[0]*len(b[0]) for _ in range(2)]
    for i in range(2):
        for j in range(len(b[0])):
            sum = 0
            for k in range(2):
                sum += a[i][k] * b[k][j]
            temp[i][j] = sum % 1000000007
    return temp

if n < 3: # n == 1, n == 2
    print(1)
else:
    print(multi(power(array, n-2), pibo)[0][0])