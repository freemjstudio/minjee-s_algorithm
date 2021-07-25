# 2751

n = int(input())
numbers = []

for i in range(n):
    x = int(input())
    numbers.append(x)

for i in sorted(numbers):
    print(i)

# 직접 merge sort 작성하기

def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array)//2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    i,j,k = 0,0,0

    while i < len(left)
