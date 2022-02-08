def binary_search(array, start, end, target):
    while start <= end:
        mid = (start + end)//2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            return binary_search(array, start, mid-1, target)
        else:
            return binary_search(array, mid+1, end, target)


a = [18.5.3