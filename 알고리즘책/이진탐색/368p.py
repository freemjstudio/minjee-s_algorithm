# 고정점 찾기

n = int(input())
array = list(map(int, input().split()))

def binary_search(start, end):
    if start > end:
        return -1
    mid = (start + end)//2
    if array[mid] == mid:
        return mid
    elif array[mid] < mid:
        return binary_search(mid+1, end)
    else:
        return binary_search(start, mid-1)

result = binary_search(0, n-1)

if result >= 0:
    print(result)
else:
    print(-1)


