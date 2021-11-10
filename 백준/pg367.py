n, x = map(int, input().split())
numbers = list(map(int, input().split()))
count = 0

def binary(array, target, start, end):
    global count;
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            count += 1
            binary(array, target, start, mid-1)
            binary(array, target, mid + 1, end)
        elif array[mid] > target:
            end = mid -1
        else:
            start = mid + 1


binary(numbers, x, 0, n-1)

