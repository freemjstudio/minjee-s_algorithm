# 9663 N-Queen
n = int(input())
result = 0
a = [False]*n
b = [False]*(2*n-1) # 대각선에 올 수 있는 가짓수
c = [False]*(2*n-1)

def solve(i):
    global result
    if i == n:
        result += 1
        return
    for j in range(n):
        if not (a[j] or b[i+j] or c[i-j+n-1]): # 각각 다 false 이면
            a[j] = b[i+j] = c[i-j+n-1] = True # 세로 방향 확인, / 대각선, \ 대각선에 퀸 추가
            solve(i+1)
            a[j] = b[i+j] = c[i-j+n-1] = False



solve(0)
print(result)
