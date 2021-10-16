# 14888 연산자 끼워넣기
import sys
input = sys.stdin.readline

def cal(num, idx, add, sub, multi, division):
    global n, maxv, minv
    if idx == n:
        maxv = max(num, maxv)
        minv = min(num, minv)
        return
    else:
        if add:
            cal(num + numbers[idx], idx+1, add-1, sub, multi, division)
        if sub:
            cal(num - numbers[idx], idx + 1, add, sub-1, multi, division)
        if multi:
            cal(num * numbers[idx], idx + 1, add, sub, multi-1, division)
        if division:
            cal(int(num/numbers[idx]), idx + 1, add, sub, multi, division-1)

maxv = -sys.maxsize -1
minv = sys.maxsize

n = int(input().strip())
numbers = list(map(int, input().split())) # 숫자 입력
a,b,c,d = map(int, input().strip().split())
cal(numbers[0], 1, a,b,c,d)
print(maxv)
print(minv)


