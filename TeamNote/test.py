# bear robotics

def binary_search(start, end, array, target):
    if start >= end:
        return -1
    mid = (start + end)//2
    if array[mid] == target:
        return mid
    elif array[mid] < target:
        return binary_search(mid +1, end, array, target)
    else:
        return binary_search(start, mid-1, array, target)

a = [1,2,3,4,5]
a.sort()

index = binary_search(0, len(a), a, 1)
print(a[index])