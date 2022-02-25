# 10815 숫자카드

n = int(input())
card = list(map(int, input().split()))
m = int(input())
find = list(map(int, input().split()))
card.sort()

def bisect(left, right, target):

    if left > right:
        return None
    mid = (left + right) // 2
    if target == card[mid]:
        return mid
    elif card[mid] < target:
        return bisect(mid+1, right, target)
    else:
        return bisect(left, mid - 1, target)

for i in find:
    result = bisect(0, n-1, i)
    if result == None:
        print('0',end=' ')
    else:
        print('1', end=' ')

