# def binary_search(array, target, start, end):
#     if start > end:
#         return None
#     mid = (start + end)//2
#     if array[mid] == target:
#         return mid
#     elif array[mid] < target:
#         return binary_search(array, target, mid+1, end)
#     else:
#         return binary_search(array, target, start, mid-1)
#
a = [0,1,2,3,4,5,6,7,8,9,10,11,12,13]
#
#
# print(binary_search(a, 10, 0, 12))

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid -1

print(binary_search(a, 10, 0, 12))
