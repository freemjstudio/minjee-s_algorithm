n = int(input())
array = list(map(int, input()))

def binary(array, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    if array[mid] == mid:
        return mid
    elif array[mid] < mid:
        binary(array, mid+1, end)
    else:
        binary(array, start, mid-1)

count = binary(array, 0, n-1)

if count == 0:
    print(-1)
else:
    print(count)


