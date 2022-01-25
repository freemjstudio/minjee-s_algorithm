n, x = map(int, input().split())
array = list(map(int, input().split()))

count = 0

def count_by_value(start, end, target):
    a = first(start, end, target)
    if a == None:
        return 0
    b = last(start, end, target)
    return b - a +1

def first(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    # 해당 값을 가지는 원소 중에서 가장 왼쪽에 있는 경우에만 인덱스 반환
    if mid == 0 or array[mid] == target and target > array[mid-1]:
        return mid
    elif array[mid] >= target:
        return first(array, target, start, mid-1)
    else:
        return first(array, target, mid+1, end)

def last(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    if mid == n-1 or array[mid] == target and target < array[mid+1]:
        return mid
    elif array[mid] > target:
        return last(array, target, start, mid-1)
    else:
        return last(array, target, mid+1, end)


def binary_search(start, end, target):
    mid = (start+end)//2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(start, mid-1, target)
    else:
        return binary_search(mid+1, end, target)

if count == 0:
    print(-1)
else:
    print(count)