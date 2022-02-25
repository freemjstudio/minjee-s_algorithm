# 10815 숫자카드

n = int(input())
card = list(map(int, input().split()))
m = int(input())
find = list(map(int, input().split()))

for i in find:
    if i in card:
        print('1', end=' ')
    else:
        print('0', end=' ')